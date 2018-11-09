from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet, ProductViewSet


master_router = DefaultRouter()

# ユーザーマスタ
master_router.register(r'users', UserViewSet)
# 顧客マスタ
master_router.register(r'customers', CustomerViewSet)
# 製品マスタ（サンプル用本当はいらない）
master_router.register(r'products', ProductViewSet)