from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

