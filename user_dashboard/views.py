from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer
from listing.models import ListingCategory
from .serializers import ListingCategorySerializer
from rest_framework import generics


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "email": user.email,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# List and Create API for ListingCategory
class ListingCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer

# Retrieve, Update, and Delete API for ListingCategory
class ListingCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingCategory.objects.all()
    serializer_class = ListingCategorySerializer