from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated

from listing.models import ListingCategory
from .serializers import ListingCategorySerializer,LoginSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            if not user.is_staff:  
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "token": token.key,
                        "username": user.username,
                        "email": user.email,
                        "user_type": "user",
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"detail": "Access denied. You must be a regular user."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User logout 
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)  
            token.delete()  
            return Response(
                {"detail": "Successfully logged out."},
                status=status.HTTP_200_OK,
            )
        except Token.DoesNotExist:
            return Response(
                {"detail": "Token not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

# List and Create API for ListingCategory
class ListingCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer

# Retrieve, Update, and Delete API for ListingCategory
class ListingCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer

