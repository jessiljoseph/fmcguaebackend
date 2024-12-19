from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from listing.models import ListingCategory, Keywords, ListingBrands, Packages, Organization, \
    ListingReviews, ListingEnquiry, Advertisements, Insight
from products.models import ProductCategory, ProductEnquriy, Product, ProductImage, ProductReviews
from .serializers import (UserSerializer,
    LoginSerializer, ListingCategorySerializer,
    KeywordsSerializer, ListingBrandsSerializer, PackagesSerializer, OrganizationSerializer, ListingReviewsSerializer,
    ListingEnquirySerializer, AdvertisementsSerializer, ProductCategorySerializer, ProductEnquirySerializer,
    ProductSerializer, ProductImageSerializer, ProductReviewsSerializer, InsightSerializer
)

class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admins can access

    def get(self, request):
        users = User.objects.all()  # Fetch all users
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admins can access

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

class SuperAdminLoginAPIView(APIView):
    permission_classes = [IsAdminUser]  # Only admins can log in

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)  # Log the user in via session (optional if using tokens)
            
            # Create or retrieve the user token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "email": user.email,
                    "user_type": "admin",  # Denote the user as an admin
                },
                status=200,
            )
        return Response(serializer.errors, status=400)

# Superadmin Logout View
class SuperAdminLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)  
            token.delete()  # Delete the token
            logout(request)  # Log the user out (optional if using token auth)
            
            return Response(
                {"message": "Successfully logged out."},
                status=200,
            )
        except Token.DoesNotExist:
            return Response(
                {"detail": "Token not found."},
                status=400,
            )

# List all ListingCategory entries
class ListingCategoryListView(generics.ListAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer



class ListingCategoryCreateView(generics.CreateAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer
   


class ListingCategoryUpdateView(generics.UpdateAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer



class ListingCategoryDeleteView(generics.DestroyAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer



# List all Keywords entries
class KeywordsListView(generics.ListAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordsSerializer
   
# Create a new Keywords entry
class KeywordsCreateView(generics.CreateAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordsSerializer
 

   
# Update an existing Keywords entry
class KeywordsUpdateView(generics.UpdateAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordsSerializer
    

# Delete an existing Keywords entry
class KeywordsDeleteView(generics.DestroyAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordsSerializer
   


# ListingBrands Views
class ListingBrandsListView(generics.ListAPIView):
    queryset = ListingBrands.objects.all()
    serializer_class = ListingBrandsSerializer


class ListingBrandsCreateView(generics.CreateAPIView):
    queryset = ListingBrands.objects.all()
    serializer_class = ListingBrandsSerializer


class ListingBrandsUpdateView(generics.UpdateAPIView):
    queryset = ListingBrands.objects.all()
    serializer_class = ListingBrandsSerializer

class ListingBrandsDeleteView(generics.DestroyAPIView):
    queryset = ListingBrands.objects.all()
    serializer_class = ListingBrandsSerializer
  


# Packages Views
class PackagesListView(generics.ListAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer
   

class PackagesCreateView(generics.CreateAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer
  

class PackagesUpdateView(generics.UpdateAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer


class PackagesDeleteView(generics.DestroyAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer
    


# List all Organization entries

class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer






class OrganizationCreateView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    

class OrganizationUpdateView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
class OrganizationDeleteView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
   
# List all reviews
class ListingReviewsListView(generics.ListAPIView):
    queryset = ListingReviews.objects.all()
    serializer_class = ListingReviewsSerializer
   
class ListingReviewsCreateView(generics.CreateAPIView):
    queryset = ListingReviews.objects.all()
    serializer_class = ListingReviewsSerializer
 
class ListingReviewsUpdateView(generics.UpdateAPIView):
    queryset = ListingReviews.objects.all()
    serializer_class = ListingReviewsSerializer
   
class ListingReviewsDeleteView(generics.DestroyAPIView):
    queryset = ListingReviews.objects.all()
    serializer_class = ListingReviewsSerializer
  

# List all enquiries
class ListingEnquiryListView(generics.ListAPIView):
    queryset = ListingEnquiry.objects.all()
    serializer_class = ListingEnquirySerializer
  



class ListingEnquiryCreateView(generics.CreateAPIView):
    queryset = ListingEnquiry.objects.all()
    serializer_class = ListingEnquirySerializer
   
class ListingEnquiryUpdateView(generics.UpdateAPIView):
    queryset = ListingEnquiry.objects.all()
    serializer_class = ListingEnquirySerializer
  
class ListingEnquiryDeleteView(generics.DestroyAPIView):
    queryset = ListingEnquiry.objects.all()
    serializer_class = ListingEnquirySerializer
   
# List all advertisements
class AdvertisementsListView(generics.ListAPIView):
    queryset = Advertisements.objects.all()
    serializer_class = AdvertisementsSerializer

class AdvertisementsCreateView(generics.CreateAPIView):
    queryset = Advertisements.objects.all()
    serializer_class = AdvertisementsSerializer


class AdvertisementsUpdateView(generics.UpdateAPIView):
    queryset = Advertisements.objects.all()
    serializer_class = AdvertisementsSerializer


class AdvertisementsDeleteView(generics.DestroyAPIView):
    queryset = Advertisements.objects.all()
    serializer_class = AdvertisementsSerializer


#productcategory views
class ProductCategoryListView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryCreateView(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryUpdateView(generics.UpdateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDeleteView(generics.DestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


#product api views

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageListView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageCreateView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageUpdateView(generics.UpdateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageDeleteView(generics.DestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ProductReviewsListView(generics.ListAPIView):
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer
   

class ProductReviewsCreateView(generics.CreateAPIView):
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer
    
class ProductReviewsUpdateView(generics.UpdateAPIView):
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer
  

class ProductReviewsDeleteView(generics.DestroyAPIView):
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer

class ProductEnquiryListView(generics.ListAPIView):
    queryset = ProductEnquriy.objects.all()
    serializer_class = ProductEnquirySerializer


class ProductEnquiryCreateView(generics.CreateAPIView):
    queryset = ProductEnquriy.objects.all()
    serializer_class = ProductEnquirySerializer

class ProductEnquiryUpdateView(generics.UpdateAPIView):
    queryset = ProductEnquriy.objects.all()
    serializer_class = ProductEnquirySerializer


class ProductEnquiryDeleteView(generics.DestroyAPIView):
    queryset = ProductEnquriy.objects.all()
    serializer_class = ProductEnquirySerializer



# View to create a new insight
class InsightCreateView(generics.CreateAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

class InsightListView(generics.ListAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

    

class InsightUpdateView(generics.UpdateAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

class InsightDeleteView(generics.DestroyAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
