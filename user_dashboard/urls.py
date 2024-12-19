from django.urls import path
from fmcguae import settings
from django.conf.urls.static import static
from .views import ProfileView,ListingCategoryDetailAPIView, ListingCategoryListCreateAPIView, UserLoginAPIView,UserLogoutAPIView

urlpatterns = [
    path('user/login/', UserLoginAPIView.as_view(), name='user_login'),
    path('user/logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path("profile/", ProfileView.as_view(), name="profile"),

    path('users/categories/', ListingCategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('users/categories/<int:pk>/', ListingCategoryDetailAPIView.as_view(), name='category_detail'),
    
    path('users/keywords/<int:pk>/', ListingCategoryDetailAPIView.as_view(), name='category_detail'),
]


if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
