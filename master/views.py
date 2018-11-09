from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from .models import AppUser, Customer, Product
from .serializers import UserSerializer, CustomerSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


class CustomerFilter(filters.FilterSet):
    """顧客検索条件用フィルタークラス"""
    
    name = filters.CharFilter(lookup_expr='contains')
    created_at_from = filters.CharFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = filters.CharFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Customer
        fields = ['name', 'created_at_from', 'created_at_to']


class ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_class = CustomerFilter
