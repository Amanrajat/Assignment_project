from django.contrib import admin
from .models import User_Model, Product_Model, Order_Model



@admin.register(User_Model)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Product_Model)
class ProductAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return super().get_queryset(request).using('products_db')

    def save_model(self, request, obj, form, change):
        obj.save(using='products_db')

    def delete_model(self, request, obj):
        obj.delete(using='products_db')


@admin.register(Order_Model)
class OrderAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return super().get_queryset(request).using('orders_db')

    def save_model(self, request, obj, form, change):
        obj.save(using='orders_db')

    def delete_model(self, request, obj):
        obj.delete(using='orders_db')
