from rest_framework.viewsets import ModelViewSet
from .models import User_Model, Product_Model, Order_Model
from .serializers import UserSerializer, ProductSerializer, OrderSerializer

class UserViewSet(ModelViewSet):
    queryset = User_Model.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product_Model.objects.using('products_db').all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
       Product_Model.objects.using('products_db').create(**serializer.validated_data)


class OrderViewSet(ModelViewSet):
    queryset = Order_Model.objects.using('orders_db').all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        Order_Model.objects.using('orders_db').create(**serializer.validated_data)
