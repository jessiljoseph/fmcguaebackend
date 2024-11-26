import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail 
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .models import Insight, ListingCategory, Organization, Packages, Partner, Testimonial
from .serializers import CategorySerializer, InsightSerializer, OrganizationSerializer, PackageSerializer, PartnerSerializer, TestimonialSerializer

class CategoryListView(generics.ListAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'  

class PackageCreateView(generics.ListAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Handle additional logic here if needed (e.g., email verification)
        return super().create(request, *args, **kwargs)            
            
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
    lookup_field = 'slug'  
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

