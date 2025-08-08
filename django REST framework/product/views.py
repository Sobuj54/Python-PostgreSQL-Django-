from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product, Category
from .serializers import ProductSerializer , CategorySerializer, CategoryListSerializer
from rest_framework import status
from django.db.models import Count

# Create your views here.
# product views
@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
            product = Product.objects.select_related("category") # optimized query
            # product = Product.objects.all() unoptimzed
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)
    if request.method == 'POST':
         serializer = ProductSerializer(data=request.data) # deserialization
         if serializer.is_valid():
            #   print(serializer.validated_data)
              serializer.save()

              return Response(serializer.data)
         else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_product(request, id):
     # product = Product.objects.select_related("category").get(pk=1)
    product = get_object_or_404(Product.objects.select_related("category"), pk=id)
    if request.method == 'GET':
          serializer = ProductSerializer(product)
          return Response(serializer.data)
    if request.method == 'PUT':
         serializer = ProductSerializer(product, data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
    if request.method == "DELETE" :
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
 


# category views
@api_view(['GET'])
def view_categories(request):
    categories = Category.objects.annotate(total_products=Count("products"))
    # categories = Category.objects.all() unoptimized
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_specific_category(request, id):
    category = get_object_or_404(Category.objects.prefetch_related('products'), pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
