from django.contrib.auth import authenticate
from rest_framework import serializers

from listing.models import ListingCategory

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        
        return {"user": user}

class ListingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingCategory
        fields = '__all__'