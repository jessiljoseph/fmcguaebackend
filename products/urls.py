from django.urls import path
from django.conf.urls.static import static

from fmcguae import settings

from .views import (
    ProductCategoryListView, ProductListView, ProductDetailView, 
    ProductImageListView, ProductReviewsListView, ProductEnquiryListView
)

urlpatterns = [
    path('api/categories/', ProductCategoryListView.as_view(), name='product_category_list'),
    path('api/products/', ProductListView.as_view(), name='product_list'),
    path('api/products/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/product-images/', ProductImageListView.as_view(), name='product_image_list'),
    path('api/product-reviews/', ProductReviewsListView.as_view(), name='product_reviews_list'),
    path('api/product-enquiries/', ProductEnquiryListView.as_view(), name='product_enquiry_list'),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)