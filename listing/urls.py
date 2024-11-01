from django.urls import path
from .views import AllCategoriesView, InsightListView, InsightsDetailView, PackageCreateView, PartnerListView, TestimonialListView
from django.conf.urls.static import static

from fmcguae import settings

urlpatterns = [
    path('api/categories/all/', AllCategoriesView.as_view(), name='all_categories'),
    path('api/package/', PackageCreateView.as_view(), name='packages'),
    path('api/testimonials/', TestimonialListView.as_view(), name='testimonial_list'),
    path('api/partners/', PartnerListView.as_view(), name='partner_list'),
    path('api/insights/', InsightListView.as_view(), name='insight_list'),
    path('api/insights/<slug:slug>/', InsightsDetailView.as_view(), name='insight_detail'),

]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)