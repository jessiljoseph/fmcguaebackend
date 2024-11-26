from django.urls import path
from .views import ListingCategoryDetailAPIView, ListingCategoryListCreateAPIView, LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/categories/', ListingCategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('users/categories/<int:pk>/', ListingCategoryDetailAPIView.as_view(), name='category_detail'),
]
