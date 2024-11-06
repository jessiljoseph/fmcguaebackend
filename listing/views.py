from rest_framework import generics, viewsets
from .models import Insight, ListingCategory, Organization, Packages, Partner, Testimonial
from .serializers import CategorySerializer, InsightSerializer, OrganizationSerializer, PackageSerializer, PartnerSerializer, TestimonialSerializer


class AllCategoriesView(generics.ListAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = CategorySerializer

class PackageCreateView(generics.ListAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
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

