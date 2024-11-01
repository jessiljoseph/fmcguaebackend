from rest_framework import generics
from .models import Insight, ListingCategory, Packages, Partner, Testimonial
from .serializers import CategorySerializer, InsightSerializer, PackageSerializer, PartnerSerializer, TestimonialSerializer


class AllCategoriesView(generics.ListAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = CategorySerializer

class PackageCreateView(generics.ListAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer

class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class InsightListView(generics.ListAPIView):
    queryset = Insight.objects.filter(status='approved').order_by('-created')
    serializer_class = InsightSerializer    

class InsightsDetailView(generics.RetrieveAPIView):
    queryset = Insight.objects.all
    serializer_class = InsightSerializer  
    lookup_field = 'slug'  
