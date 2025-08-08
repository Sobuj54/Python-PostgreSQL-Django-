from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product, Category
from .serializers import ProductSerializer , CategorySerializer
from rest_framework import status

# Create your views here.
# product views
@api_view(['GET'])
def view_products(request):
    product = Product.objects.select_related("category").all() # optimized query
    # product = Product.objects.all() unoptimzed
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def view_specific_product(request, id):
     # product = Product.objects.select_related("category").get(pk=1)
    product = get_object_or_404(Product.objects.select_related("category"), pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
 


# category views
@api_view()
def view_categories(request):
    return Response({"message": "category view"})

@api_view(['GET'])
def view_specific_category(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
