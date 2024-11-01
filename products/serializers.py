from rest_framework import serializers
from .models import ProductCategory, Product, ProductImage, ProductReviews, ProductEnquriy

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'image', 'slug', 'seo_title', 'seo_description', 'image_alt', 'created', 'updated']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'products']

class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviews
        fields = ['id', 'products', 'rating', 'subject', 'comment', 'created', 'updated', 'status']

class ProductEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnquriy
        fields = ['id', 'products', 'name', 'email', 'mobile', 'subject', 'message', 'status']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(many=True)
    images = ProductImageSerializer(many=True, source='productimage_set', read_only=True)
    reviews = ProductReviewsSerializer(many=True, source='productreviews_set', read_only=True)
    enquiries = ProductEnquirySerializer(many=True, source='productenquriy_set', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'name', 'organization', 'description', 'offer_price', 'sales_price', 
            'created_at', 'updated_at', 'status', 'keywords', 'images', 'reviews', 'enquiries'
        ]
