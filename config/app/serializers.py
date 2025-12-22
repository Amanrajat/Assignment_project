from rest_framework import serializers
from .models import User_Model, Product_Model,Order_Model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        fields = '__all__'

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Model
        fields = '__all__' 

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value   
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Model
        fields = '__all__'

    def validate(self, data):
        user_id = data.get("user_id")
        product_id = data.get("product_id")
        quantity = data.get("quantity")

        # Check User exists (users.db)
        if not User_Model.objects.using('default').filter(id=user_id).exists():
            raise serializers.ValidationError({
                "user_id": "User does not exist in users database"
            })

        # Check Product exists (products.db)
        if not Product_Model.objects.using('products_db').filter(id=product_id).exists():
            raise serializers.ValidationError({
                "product_id": "Product does not exist in products database"
            })

        # Quantity validation
        if quantity <= 0:
            raise serializers.ValidationError({
                "quantity": "Quantity must be greater than 0"
            })

        return data