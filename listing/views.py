from rest_framework import generics
from .models import ListingCategory, Packages, Partner, Testimonial
from .serializers import CategorySerializer, PackageSerializer, PartnerSerializer, TestimonialSerializer


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