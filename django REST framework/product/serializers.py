from rest_framework import serializers
from .models import Product, Category
from decimal import Decimal

class CategoryListSerializer(serializers.ModelSerializer):
    total_products = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    #  method name will be get_<field name>
    def get_price_with_tax(self, product):
        return round(product.price * Decimal(1.1),2)
    
    # write with category ID
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    # read with full category object
    category = CategorySerializer(read_only=True)
    
    # this will show only the category name
    # category = serializers.StringRelatedField()  # uses __str__ method of Category

    class Meta:
        model = Product
        fields = "__all__"

    # field level validation
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("price can't be negative.")
        return price

