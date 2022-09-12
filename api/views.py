from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import CoinAddress, User
from .serializers import UserSerializer, CoinAddressSerializer
from .utilities import retrieve_address_data, retrieve_multi_address_data

# User API endpoints

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_fields = ('email')

# Coin Address API endpoints

@api_view(['GET', 'POST'])
def coin_address_list(request, user_id):
    """
    Get or add coin addresses for the given user.
    """
    if request.method == 'GET':
        addresses = CoinAddress.objects.filter(owner=user_id)
        serializer = CoinAddressSerializer(addresses, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if request.data and request.data.get("addresses"):
            results = retrieve_multi_address_data(request.data["addresses"])
            print(results)
            for address_data in results:
                address_data['owner'] = user_id
                serializer = CoinAddressSerializer(data=address_data)
                if serializer.is_valid():
                    serializer.save()
            if not serializer.errors:
                addresses = CoinAddress.objects.filter(owner=user_id)
                serializer = CoinAddressSerializer(addresses, many=True)
                return Response(serializer.data)
            else:    
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def coin_address_detail(request, user_id, address):
    """ 
    Get, add or delete a coin address for the given user.
    """
    if request.method == 'GET':
        try:
            address_obj = CoinAddress.objects.get(address=address)
        except CoinAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        response_data = retrieve_address_data(address)
        return Response(response_data)
    
    elif request.method == 'POST':
        data = retrieve_address_data(address)
        data['owner'] = user_id
        serializer = CoinAddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            address_obj = CoinAddress.objects.get(address=address)
        except CoinAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        address_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
