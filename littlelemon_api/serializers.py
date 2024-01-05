from rest_framework import serializers
from .models import MenuItem,Order,OrderItem,User,Cart,Category
#ModelSerializer class will auto generate all the corresponding model fields
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','featured','category']
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user','menuitem','quantity','unit_price','price']
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','delivery_crew','status','total','date']
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','order','menuitem','quantity','unit_price','price']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
