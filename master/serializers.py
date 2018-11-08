from rest_framework import serializers
from .models import Customer, Product
from django.contrib.auth.models import User
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name')


class ProductSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'customer', 'name', 'unit_price', 'unit')


class CustomerSerializer(WritableNestedModelSerializer):
    product = ProductSerializer(many=True, allow_null=True, source='products')

    class Meta:
        model = Customer
        fields = ('id', 'name', 'rank', 'user', 'created_at', 'product',)
