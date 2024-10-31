from rest_framework import generics
from .models import ListingCategory, Packages, Testimonial
from .serializers import CategorySerializer, PackageSerializer, TestimonialSerializer


class AllCategoriesView(generics.ListAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = CategorySerializer

class PackageCreateView(generics.ListAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer

class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    #testmonial