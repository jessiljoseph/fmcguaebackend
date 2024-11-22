from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('superadmin.urls')),
    path('', include('listing.urls')),
    path('', include('products.urls')),
     path('', include('user_dashboard.urls')),
    path('api/login/', obtain_auth_token, name='api_login'),

]
