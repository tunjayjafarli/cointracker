from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # returns all addresses for the given user
    path('user/<int:user_id>/wallet/', views.coin_address_list),

    # returns the specific address matching query 
    path('user/<int:user_id>/wallet/<address>', views.coin_address_detail),
]