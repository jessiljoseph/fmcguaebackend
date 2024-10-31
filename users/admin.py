from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('country', 'phone_number')}),  # Include the country and phone number fields
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('country', 'phone_number')}),  # Add country and phone number to user creation form
    )
    list_display = ('username', 'email', 'country', 'phone_number', 'is_staff', 'is_active')  # Customize the display in the user list
