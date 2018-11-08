from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from .views import CustomerViewSet


master_router = DefaultRouter()

# 顧客マスタ
master_router.register(r'customers', CustomerViewSet)
# 製品マスタ（サンプル用本当はいらない）
master_router.register(r'products', ProductViewSet)