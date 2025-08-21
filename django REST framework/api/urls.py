from django.urls import path, include
from product.views import ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls))
]

# urlpatterns = [
#     path("products/", include("product.product_urls")),
#     path("categories/", include("product.category_urls"))
# ]