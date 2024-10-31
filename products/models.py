from django.db import models

from listing.models import Organization, Keywords


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='Product Category' ,blank=True, null=True )
    slug = models.SlugField(unique=True)
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    image_alt = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICE = [
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ]
    category = models.ManyToManyField(ProductCategory)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,  null=True, blank=True)
    description = models.TextField()
    offer_price = models.IntegerField()
    sales_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICE)
    keywords = models.ManyToManyField(Keywords)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='Product Image')

    def __str__(self):
        return self.products.name
class ProductReviews(models.Model):
    STATUS_CHOICE = [
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ]
    products = models.ForeignKey(Product, on_delete=models.CASCADE,  null=True, blank=True)
    rating = models.PositiveIntegerField(default=5, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICE)

    def __str__(self):
        return self.products.name
class ProductEnquriy(models.Model):
    STATUS_CHOICE = [
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ]
    products = models.ForeignKey(Product, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICE)

    def __str__(self):
        return self.products.name

