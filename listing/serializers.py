from rest_framework import serializers
from .models import Insight, ListingCategory, Organization, Packages, Partner, Testimonial

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingCategory
        fields = ['name', 'image']


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

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'         


class InsightSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    class Meta:
        model = Insight
        fields = ['organization', 'category', 'title', 'image', 'description', 'created', 'updated', 'slug']

