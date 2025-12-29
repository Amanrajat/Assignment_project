from rest_framework.viewsets import ModelViewSet
from django.db import transaction
from .models import User_Model, Product_Model, Order_Model
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from rest_framework.exceptions import ValidationError

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
        user_id = serializer.validated_data["user_id"]
        product_id = serializer.validated_data["product_id"]
        quantity = serializer.validated_data["quantity"]

       
        with transaction.atomic(using='products_db'):

            
            product = Product_Model.objects.using('products_db') \
                .select_for_update() \
                .get(id=product_id)

          
            if product.quantity < quantity:
                raise ValidationError("Product out of stock")

           
            product.quantity -= quantity
            product.save(using='products_db')

        
        Order_Model.objects.using('orders_db').create(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )