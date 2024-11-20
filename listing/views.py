import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail 
from rest_framework.permissions import AllowAny
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
        # Prepare dynamic data for the template
        dynamic_data = {
            "company_name": Organization.company_name,
        }

        # Set up the email with SendGrid
        message = Mail(
            from_email='no-reply@yourdomain.com',
            to_emails=Organization.company_email,
            subject=f"Welcome to Our Platform, {Organization.company_name}",
            html_content='<strong>Thank you for joining us!</strong>'
        )

        message.dynamic_template_data = dynamic_data
        message.template_id = 'YOUR_SENDGRID_TEMPLATE_ID'

        try:
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            sg.send(message)
        except Exception as e:
            print(f"Error sending email: {e}")

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

