# views.py
from rest_framework import generics
from .models import ProductCategory, Product, ProductImage, ProductReviews, ProductEnquriy
from .serializers import (
    ProductCategorySerializer, ProductSerializer, ProductImageSerializer, 
    ProductReviewsSerializer, ProductEnquirySerializer
)

class ProductCategoryListView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductImageListView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductReviewsListView(generics.ListCreateAPIView):
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer

class ProductEnquiryListView(generics.ListCreateAPIView):
    queryset = ProductEnquriy.objects.all()
    serializer_class = ProductEnquirySerializer

