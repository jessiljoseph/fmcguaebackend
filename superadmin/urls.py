from django.urls import path
from django.conf.urls.static import static


from fmcguae import settings
from superadmin.views import CountryListView, CountryCreateView, CountryUpdateView, \
    CountryDeleteView, AdminLoginView, AdminLogoutView, StateListView, StateCreateView, StateUpdateView, \
    StateDeleteView, ListingIsoListView, ListingIsoCreateView, ListingIsoUpdateView, \
    ListingIsoDeleteView, ListingCategoryListView, ListingCategoryCreateView, ListingCategoryUpdateView, \
    ListingCategoryDeleteView, KeywordsListView, KeywordsCreateView, KeywordsDeleteView, KeywordsUpdateView, \
    ListingBrandsDeleteView, ListingBrandsListView, ListingBrandsCreateView, ListingBrandsUpdateView, \
    PackagesCreateView, PackagesListView, PackagesUpdateView, PackagesDeleteView, OrganizationListView, \
    OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, ListingReviewsListView, \
    ListingReviewsCreateView, ListingReviewsUpdateView, ListingReviewsDeleteView, ListingEnquiryListView, \
    ListingEnquiryCreateView, ListingEnquiryUpdateView, ListingEnquiryDeleteView, AdvertisementsListView, \
    AdvertisementsCreateView, AdvertisementsUpdateView, AdvertisementsDeleteView, InsightListView, InsightCreateView, \
    InsightUpdateView, InsightDeleteView
from .views import (
    ProductCategoryListView, ProductCategoryCreateView, ProductCategoryUpdateView, ProductCategoryDeleteView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductImageListView, ProductImageCreateView, ProductImageUpdateView, ProductImageDeleteView,
    ProductReviewsListView, ProductReviewsCreateView, ProductReviewsUpdateView, ProductReviewsDeleteView,
    ProductEnquiryListView, ProductEnquiryCreateView, ProductEnquiryUpdateView, ProductEnquiryDeleteView
)

urlpatterns = [
    path('api/login/', AdminLoginView.as_view(), name='admin.login'),
    path('api/logout/', AdminLogoutView.as_view(), name='admin.logout'),

    path('api/countries/list/', CountryListView.as_view(), name='admin.country_list'),
    path('api/countries/create/', CountryCreateView.as_view(), name='admin.country_create'),
    path('api/countries/update/<int:pk>/', CountryUpdateView.as_view(), name='admin.country_update'),
    path('api/countries/delete/<int:pk>/', CountryDeleteView.as_view(), name='admin.country_delete'),

    path('api/state/list/', StateListView.as_view(), name='admin.state_list'),
    path('api/state/create/', StateCreateView.as_view(), name='admin.state_create'),
    path('api/state/update/<int:pk>/', StateUpdateView.as_view(), name='admin.state_update'),
    path('api/state/delete/<int:pk>/', StateDeleteView.as_view(), name='admin.state_delete'),

    path('api/listing_iso/list/', ListingIsoListView.as_view(), name='admin.listing_iso_list'),
    path('api/listing_iso/create/', ListingIsoCreateView.as_view(), name='admin.listing_iso_create'),
    path('api/listing_iso/update/<int:pk>/', ListingIsoUpdateView.as_view(), name='admin.listing_iso_update'),
    path('api/listing_iso/delete/<int:pk>/', ListingIsoDeleteView.as_view(), name='admin.listing_iso_delete'),

    path('api/listing_category/list/', ListingCategoryListView.as_view(), name='admin.listing_category_list'),
    path('api/listing_category/create/', ListingCategoryCreateView.as_view(), name='admin.listing_category_create'),
    path('api/listing_category/update/<int:pk>/', ListingCategoryUpdateView.as_view(), name='admin.listing_category_update'),
    path('api/listing_category/delete/<int:pk>/', ListingCategoryDeleteView.as_view(), name='admin.listing_category_delete'),

    path('api/keywords/list/', KeywordsListView.as_view(), name='admin.keywords_list'),
    path('api/keywords/create/', KeywordsCreateView.as_view(), name='admin.keywords_create'),
    path('api/keywords/update/<int:pk>/', KeywordsUpdateView.as_view(), name='admin.keywords_update'),
    path('api/keywords/delete/<int:pk>/', KeywordsDeleteView.as_view(), name='admin.keywords_delete'),

    path('api/listing_brands/list/', ListingBrandsListView.as_view(), name='admin.listing_brands_list'),
    path('api/listing_brands/create/', ListingBrandsCreateView.as_view(), name='admin.listing_brands_create'),
    path('api/listing_brands/update/<int:pk>/', ListingBrandsUpdateView.as_view(), name='admin.listing_brands_update'),
    path('api/listing_brands/delete/<int:pk>/', ListingBrandsDeleteView.as_view(), name='admin.listing_brands_delete'),

    path('api/packages/list/', PackagesListView.as_view(), name='admin.packages_list'),
    path('api/packages/create/', PackagesCreateView.as_view(), name='admin.packages_create'),
    path('api/packages/update/<int:pk>/', PackagesUpdateView.as_view(), name='admin.packages_update'),
    path('api/packages/delete/<int:pk>/', PackagesDeleteView.as_view(), name='admin.packages_delete'),

    path('api/organization/list/', OrganizationListView.as_view(), name='admin.organization_list'),
    path('api/organization/create/', OrganizationCreateView.as_view(), name='admin.organization_create'),
    path('api/organization/update/<int:pk>/', OrganizationUpdateView.as_view(), name='admin.organization_update'),
    path('api/organization/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='admin.organization_delete'),

    path('api/listing-reviews/list/', ListingReviewsListView.as_view(), name='admin.listing_reviews_list'),
    path('api/listing-reviews/create/', ListingReviewsCreateView.as_view(), name='admin.listing_reviews_create'),
    path('api/listing-reviews/update/<int:pk>/', ListingReviewsUpdateView.as_view(), name='admin.listing_reviews_update'),
    path('api/listing-reviews/delete/<int:pk>/', ListingReviewsDeleteView.as_view(), name='admin.listing_reviews_delete'),

    path('api/listing-enquiry/list/', ListingEnquiryListView.as_view(), name='admin.listing_enquiry_list'),
    path('api/listing-enquiry/create/', ListingEnquiryCreateView.as_view(), name='admin.listing_enquiry_create'),

    path('api/listing-enquiry/update/<int:pk>/', ListingEnquiryUpdateView.as_view(), name='admin.listing_enquiry_update'),
    path('api/listing-enquiry/delete/<int:pk>/', ListingEnquiryDeleteView.as_view(), name='admin.listing_enquiry_delete'),

    path('api/advertisements/list/', AdvertisementsListView.as_view(), name='admin.advertisements_list'),
    path('api/advertisements/create/', AdvertisementsCreateView.as_view(), name='admin.advertisements_create'),
    path('api/advertisements/update/<int:pk>/', AdvertisementsUpdateView.as_view(), name='admin.advertisements_update'),
    path('api/advertisements/delete/<int:pk>/', AdvertisementsDeleteView.as_view(), name='admin.advertisements_delete'),

    # ProductCategory URLs
    path('api/product_category/list/', ProductCategoryListView.as_view(), name='admin.product_category_list'),
    path('api/product_category/create/', ProductCategoryCreateView.as_view(), name='admin.product_category_create'),
    path('api/product_category/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='admin.product_category_update'),
    path('api/product_category/delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='admin.product_category_delete'),

    # Product URLs
    path('api/product/list/', ProductListView.as_view(), name='admin.product_list'),
    path('api/product/create/', ProductCreateView.as_view(), name='admin.product_create'),
    path('api/product/update/<int:pk>/', ProductUpdateView.as_view(), name='admin.product_update'),
    path('api/product/delete/<int:pk>/', ProductDeleteView.as_view(), name='admin.product_delete'),

    # ProductImage URLs
    path('api/product_image/list/', ProductImageListView.as_view(), name='admin.product_image_list'),
    path('api/product_image/create/', ProductImageCreateView.as_view(), name='admin.product_image_create'),
    path('api/product_image/update/<int:pk>/', ProductImageUpdateView.as_view(), name='admin.product_image_update'),
    path('api/product_image/delete/<int:pk>/', ProductImageDeleteView.as_view(), name='admin.product_image_delete'),

    # ProductReviews URLs
    path('api/product_reviews/list/', ProductReviewsListView.as_view(), name='admin.product_reviews_list'),
    path('api/product_reviews/create/', ProductReviewsCreateView.as_view(), name='admin.product_reviews_create'),
    path('api/product_reviews/update/<int:pk>/', ProductReviewsUpdateView.as_view(), name='admin.product_reviews_update'),
    path('api/product_reviews/delete/<int:pk>/', ProductReviewsDeleteView.as_view(), name='admin.product_reviews_delete'),

    # ProductEnquiry URLs
    path('api/product_enquiry/list/', ProductEnquiryListView.as_view(), name='admin.product_enquiry_list'),
    path('api/product_enquiry/create/', ProductEnquiryCreateView.as_view(), name='admin.product_enquiry_create'),
    path('api/product_enquiry/update/<int:pk>/', ProductEnquiryUpdateView.as_view(), name='admin.product_enquiry_update'),
    path('api/product_enquiry/delete/<int:pk>/', ProductEnquiryDeleteView.as_view(), name='admin.product_enquiry_delete'),

    path('api/insights/list/', InsightListView.as_view(), name='admin.insight_list'),
    path('api/insights/create/', InsightCreateView.as_view(), name='admin.insight_create'),
    path('api/insights/<int:pk>/update/', InsightUpdateView.as_view(), name='admin.insight_update'),
    path('api/insights/<int:pk>/delete/', InsightDeleteView.as_view(), name='admin.insight_delete'),


]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
