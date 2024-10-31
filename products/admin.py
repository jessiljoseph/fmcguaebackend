from django.contrib import admin
from .models import Product, ProductCategory, ProductImage, ProductReviews, ProductEnquriy

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReviews)
admin.site.register(ProductEnquriy)
