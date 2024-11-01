from rest_framework import serializers
from .models import Insight, ListingCategory, Packages, Partner, Testimonial


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


class InsightSerializer(serializers.ModelSerializer):
    organization_logo = serializers.SerializerMethodField()  

    class Meta:
        model = Insight
        fields = ['organization_logo', 'category', 'title', 'image', 'description', 'created', 'updated', 'slug']

    def get_organization_logo(self, obj):
        return obj.organization.logo.url if obj.organization and obj.organization.logo else None
