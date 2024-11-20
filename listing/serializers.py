from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
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

    package_id = serializers.PrimaryKeyRelatedField(queryset=Packages.objects.all(), source='package')
    user_username = serializers.CharField(source='user.username', read_only=True)  
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}) 

    class Meta:
        model = Organization
        fields = [
            'user_username', 'password', 'user', 'package', 'logo', 'banner', 'brochure',
            'category', 'keywords', 'brands', 
            'company_name', 'company_email', 'company_mobile', 'company_fax',
            'company_whatsapp', 'company_description', 'address', 'building_no', 
            'street', 'area', 'po_box', 'city', 'state', 'country', 
            'website', 'google_map_url', 'iso', 
            'contact_person_name', 'contact_person_email', 'contact_person_mobile',
            'facebook', 'twitter', 'linkedin', 'instagram', 'youtube', 
            'verified', 'supplier', 'distributor', 
            'start_date', 'end_date', 'slug', 'created_at', 'updated_at', 'package_id'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(username=validated_data['user'].username, password=password)
        organization = Organization.objects.create(user=user, **validated_data)
        keywords_data = validated_data.pop('keywords', [])
        brands_data = validated_data.pop('brands', [])
        
        for keyword_data in keywords_data:
            keyword = Keywords.objects.create(**keyword_data)
            organization.keywords.add(keyword)
        
        for brand_data in brands_data:
            brand = ListingBrands.objects.create(**brand_data)
            organization.brands.add(brand)

        return organization


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password field
    confirm_password = serializers.CharField(write_only=True)  # Confirm password field
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=255)
    organization_id = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email', 'organization_id']
    
    def validate(self, data):
        """
        Validate that password and confirm_password match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        """
        Create a new user and link to an organization if provided.
        """
        password = validated_data.pop('password')  # Password is already validated, so pop it
        user = User.objects.create_user(**validated_data)  # Create the user
        user.set_password(password)  # Hash the password
        user.save()

        # Link to organization if provided
        organization = validated_data.get('organization_id', None)
        if organization:
            organization.user = user
            organization.save()

        return user

        
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ['id','name', 'price', 'features']


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

