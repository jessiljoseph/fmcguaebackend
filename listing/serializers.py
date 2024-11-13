from rest_framework import serializers
from .models import Insight, Keywords, ListingBrands, ListingCategory, Organization, Packages, Partner, Testimonial

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingCategory
        fields = ['name', 'image']


class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = ['id', 'name', 'seo_title', 'seo_description', 'slug', 'section']

class ListingBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingBrands
        fields = ['id', 'name', 'seo_title', 'seo_description', 'slug']        

class OrganizationSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ListingCategory.objects.all(), many=True)
    keywords = KeywordsSerializer(many=True)
    brands = ListingBrandsSerializer(many=True)
    class Meta:
        model = Organization
        fields = '__all__'    

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'user', 'package', 'logo', 'banner', 'brochure', 
            'category', 'keywords', 'brands', 
            'company_name', 'company_email', 'company_mobile', 'company_fax', 
            'company_whatsapp', 'company_description', 'address', 'building_no', 
            'street', 'area', 'po_box', 'city', 'state', 'country', 
            'website', 'google_map_url', 'iso', 
            'contact_person_name', 'contact_person_email', 'contact_person_mobile', 
            'facebook', 'twitter', 'linkedin', 'instagram', 'youtube', 
            'verified', 'supplier', 'distributor', 
            'start_date', 'end_date', 'slug', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        keywords_data = validated_data.pop('keywords')
        brands_data = validated_data.pop('brands')
        organization = Organization.objects.create(**validated_data)
        
        # Create many-to-many relationships manually
        for keyword_data in keywords_data:
            keyword = Keywords.objects.create(**keyword_data)
            organization.keywords.add(keyword)
        
        for brand_data in brands_data:
            brand = ListingBrands.objects.create(**brand_data)
            organization.brands.add(brand)
        
        return organization

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ['name', 'price', 'features']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['name', 'image', 'position', 'description']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['logo', ]       
     

class InsightSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    class Meta:
        model = Insight
        fields = ['organization', 'category', 'title', 'image', 'description', 'created', 'updated', 'slug']

