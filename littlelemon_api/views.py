from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer,OrderSerializer,OrderItemSerializer,UserSerializer
from .models import MenuItem, Order, Cart, User
# Create your views here.
class MenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = MenuItemSerializer
    
class CartView(generics.RetrieveDestroyAPIView,generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = MenuItemSerializer 
# class UserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer     