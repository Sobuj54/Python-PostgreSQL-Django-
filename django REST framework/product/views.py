from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product, Category
from .serializers import ProductSerializer , CategorySerializer
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# doing the CRUD operation using ModelViewSet
class ProductViewSet(ModelViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     def destroy(self, request, *args, **kwargs):
          product = self.get_object()
          if product.stock > 10:
               return Response({"message": "Product with more than 10 stock can't be deleted."})
          self.perform_destroy(product)
          return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(ModelViewSet):
     queryset = Category.objects.annotate(total_products=Count("products"))
     serializer_class = CategorySerializer



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
          
# view products using mixins or generic vieew
class ProductList(ListCreateAPIView):
     def get_queryset(self):
          return Product.objects.select_related('category')
     def get_serializer_class(self):
          return ProductSerializer
     

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

# using generic view to get product details
class ProductDetails(RetrieveUpdateDestroyAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     lookup_field = "id"

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
     
# category details using generic view
class CategoryDetails(RetrieveUpdateDestroyAPIView):
     queryset = Category.objects.annotate(total_products=Count("products"))
     serializer_class = CategorySerializer
     lookup_field = "id"
