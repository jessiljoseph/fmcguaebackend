from django.contrib.auth import authenticate
from rest_framework import serializers

from listing.models import ListingCategory

# Serializer to validate user credentials during login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Get the user credentials
        username = data.get("username")
        password = data.get("password")

        # Authenticate user
        user = authenticate(username=username, password=password)

        # Check if authentication is successful
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data
    

    

class ListingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingCategory
        fields = '__all__'