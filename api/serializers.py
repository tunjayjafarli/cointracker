from rest_framework import serializers
from api.models import User, CoinAddress

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name')
        read_only_fields = ('id', 'is_staff',)


class CoinAddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoinAddress
        fields = [
            'address', 'address_hash', 'total_transactions', 'total_received', 'total_sent',
            'final_balance', 'owner'
        ]
