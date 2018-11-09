from rest_framework import serializers
from .models import AppUser, Customer, Product
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'username', 'last_name', 'first_name', 'email', 'profile_picture')


class ProductSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'customer', 'name', 'unit_price', 'unit')


class CustomerSerializer(WritableNestedModelSerializer):
    product = ProductSerializer(many=True, allow_null=True, source='products')

    class Meta:
        model = Customer
        fields = ('id', 'name', 'rank', 'user', 'created_at', 'product',)
