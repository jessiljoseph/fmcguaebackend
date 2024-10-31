from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (
    Country, State, ListingIso, ListingCategory, Keywords, ListingBrands, Packages,
    Organization, ListingReviews, ListingEnquiry, Advertisements, Insight, Testimonial
)

# Register Country Model
@admin.register(Country)
class CountryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register State Model
@admin.register(State)
class StateAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)
    list_filter = ('country',)


# Register ListingIso Model
@admin.register(ListingIso)
class ListingIsoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register ListingCategory Model
@admin.register(ListingCategory)
class ListingCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'seo_title', 'slug')
    search_fields = ('name', 'seo_title', 'slug')


# Register Keywords Model
@admin.register(Keywords)
class KeywordsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'section', 'slug')
    search_fields = ('name', 'section', 'slug')
    list_filter = ('section',)


# Register ListingBrands Model
@admin.register(ListingBrands)
class ListingBrandsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


# Register Packages Model
@admin.register(Packages)
class PackagesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'section')
    search_fields = ('name', 'section')
    list_filter = ('section',)


# Register Organization Model
@admin.register(Organization)
class OrganizationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('company_name', 'company_email', 'company_mobile', 'verified')
    search_fields = ('company_name', 'company_email', 'company_mobile')
    list_filter = ('verified', 'supplier', 'distributor')


# Register ListingReviews Model
@admin.register(ListingReviews)
class ListingReviewsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('organization', 'rating', 'status', 'created')
    search_fields = ('organization__company_name', 'rating', 'status')
    list_filter = ('status',)


# Register ListingEnquiry Model
@admin.register(ListingEnquiry)
class ListingEnquiryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('organization', 'name', 'email', 'status')
    search_fields = ('organization__company_name', 'name', 'email', 'status')
    list_filter = ('status',)


# Register Advertisements Model
@admin.register(Advertisements)
class AdvertisementsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('organization', 'package', 'status', 'start_date', 'end_date')
    search_fields = ('organization__company_name', 'package__name', 'status')
    list_filter = ('status', 'start_date', 'end_date')


@admin.register(Insight)
class InsightAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('organization', 'title', 'image', 'status')


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'position', 'description', 'created', 'updated')





