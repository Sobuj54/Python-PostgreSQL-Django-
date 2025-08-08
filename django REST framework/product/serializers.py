from rest_framework import serializers
from .models import Product, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    #  method name will be get_<field name>
    def get_price_with_tax(self, product):
        return round(product.price * Decimal(1.1),2)
    
    # this will show only the category name
    # category = serializers.StringRelatedField()  # uses __str__ method of Category

    # this will show the whole object in category field
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"

