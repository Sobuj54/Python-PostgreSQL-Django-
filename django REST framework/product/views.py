from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product, Category
from .serializers import ProductSerializer , CategorySerializer
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView

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
         
class ViewProducts(APIView):
     def get(self, request):
          product = Product.objects.select_related("category") # optimized query
          # product = Product.objects.all() unoptimzed
          serializer = ProductSerializer(product, many=True)
          return Response(serializer.data)
     
     def post(self, request):
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
    

class ViewSpecificProduct(APIView):
     def get(self, request, id):
          product = get_object_or_404(Product.objects.select_related("category"), pk=id)
          serializer = ProductSerializer(product)
          return Response(serializer.data)
     def post(self, request, id):
         serializer = ProductSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
     def delete(self, request, id):
         product = get_object_or_404(Product, pk=id)
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

# category views
@api_view(['GET'])
def view_categories(request):
    categories = Category.objects.annotate(total_products=Count("products"))
    # categories = Category.objects.all() unoptimized
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class ViewCategories(APIView):
     def get(self, request):
          categories = Category.objects.annotate(total_products=Count("products"))
          serializer = CategorySerializer(categories, many=True)
          return Response(serializer.data)

@api_view(['GET'])
def view_specific_category(request, id):
    category = get_object_or_404(Category.objects.prefetch_related('products'), pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

class ViewSpecificCategory(APIView):
     def get(self, request, id):
          category = get_object_or_404(Category.objects.annotate(total_products=Count("products")), pk=id)
          serializer = CategorySerializer(category)
          return Response(serializer.data, status=status.HTTP_200_OK)
     def post(self, request, id):
          serializer = CategorySerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
     def delete(self, request, id):
          category = get_object_or_404(Category, pk=id)
          category.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
