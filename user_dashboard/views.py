from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.authtoken.models import Token
from listing.models import ListingCategory
from .serializers import ListingCategorySerializer,LoginSerializer
from django.contrib.auth import  login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # Fetch the current logged-in user
        user = request.user
        # Return user's data (could be extended further as needed)
        user_data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return Response(user_data)

# Login View
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)  # Login the user via session (optional if using tokens)
            
            # Generate or fetch user token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "email": user.email,
                    "user_type": "user",  
                },
                status=200,
            )
        return Response(serializer.errors, status=400)

# Logout View
class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can log out

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)  # Find the token for the user
            token.delete()  # Delete the user's token
            logout(request)  # Logout the user (optional if using token auth)
            
            return Response(
                {"message": "Successfully logged out."},
                status=200,
            )
        except Token.DoesNotExist:
            return Response(
                {"detail": "Token not found."},
                status=400,
            )
        
# List and Create API for ListingCategory
class ListingCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer

# Retrieve, Update, and Delete API for ListingCategory
class ListingCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer

