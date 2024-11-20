from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllCategoriesView, InsightListView, InsightsDetailView, OrganizationViewSet, PackageCreateView, PartnerListView, TestimonialListView, UserRegistrationView
from django.conf.urls.static import static

from fmcguae import settings
router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet, basename='organization')

urlpatterns = [
    path('api/categories/all/', AllCategoriesView.as_view(), name='all_categories'),
    path('api/package/', PackageCreateView.as_view(), name='packages'),
    path('api/testimonials/', TestimonialListView.as_view(), name='testimonial_list'),
    path('api/partners/', PartnerListView.as_view(), name='partner_list'),
    path('api/insights/', InsightListView.as_view(), name='insight_list'),
    path('api/insights/<slug:slug>/', InsightsDetailView.as_view(), name='insight_detail'),
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='user_register'),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)