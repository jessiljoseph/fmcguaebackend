from rest_framework import serializers
from listing.models import ListingCategory, Keywords, ListingBrands, Packages, Organization, \
    ListingReviews, ListingEnquiry, Advertisements, Insight
from products.models import ProductCategory, Product, ProductImage, ProductReviews, ProductEnquriy


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})

 

class ListingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingCategory
        fields = '__all__'

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'


# Serializer for ListingBrands
class ListingBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingBrands
        fields = '__all__'

# Serializer for Packages
class PackagesSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Packages
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class ListingReviewsSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='organization.company_name', read_only=True)
    class Meta:
        model = ListingReviews
        fields = ['id', 'rating', 'subject', 'comment', 'created', 'updated', 'status', 'organization', 'company_name']

class ListingEnquirySerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField()
    class Meta:
        model = ListingEnquiry
        fields = '__all__'

    def get_organization_name(self, obj):
        return obj.organization.company_name if obj.organization else None

class AdvertisementsSerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField()
    package_name = serializers.SerializerMethodField()
    class Meta:
        model = Advertisements
        fields = '__all__'
    def get_organization_name(self, obj):
        return obj.organization.company_name if obj.organization else None
    def get_package_name(self, obj):
        return obj.package.name if obj.package else None

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductReviewsSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = ProductReviews
        fields = '__all__'

    def get_product_name(self, obj):
        return obj.products.name if obj.products else None

class ProductEnquirySerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField() 
    class Meta:
        model = ProductEnquriy
        fields = '__all__'  

    def get_product_name(self, obj):
        return obj.products.name if obj.products else None



class InsightSerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField()
    class Meta:
        model = Insight
        fields = '__all__'

    def get_organization_name(self, obj):
        return obj.organization.company_name if obj.organization else None


   
