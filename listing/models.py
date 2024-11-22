from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ListingIso(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ListingCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='Listing Category', blank=True, null=True)
    slug = models.SlugField(unique=True)
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    image_alt = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Keywords(models.Model):
    SECTION_CHOICE = [
        ('Organization', 'Organization'),
        ('Products', 'Products'),
    ]
    name = models.CharField(max_length=255)
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    slug = models.SlugField(unique=True)
    section = models.CharField(max_length=25, choices=SECTION_CHOICE)

    def __str__(self):
        return self.name

class ListingBrands(models.Model):
    name = models.CharField(max_length=255)
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Packages(models.Model):
    SECTION_CHOICE = [
        ('Organization', 'Organization'),
        ('Advertisements', 'Advertisements'),
    ]
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    features = RichTextField()
    section = models.CharField(max_length=25, choices=SECTION_CHOICE)

    def __str__(self):
        return self.name

class Organization(models.Model):
    YES_NO_CHOICE = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, null=True, blank=True)

    logo = models.FileField(upload_to='Organization/Logo')
    banner = models.FileField(upload_to='Organization/Banner')
    brochure = models.FileField(upload_to='Organization/Brochure', null=True, blank=True)

    category = models.ManyToManyField(ListingCategory)
    keywords = models.ManyToManyField(Keywords)
    brands = models.ManyToManyField(ListingBrands)

    company_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_mobile = models.CharField(max_length=255)
    company_fax = models.CharField(max_length=255)
    company_whatsapp = models.CharField(max_length=255)
    company_description = models.TextField()

    address = models.CharField(max_length=255)
    building_no = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    po_box = models.CharField(max_length=25)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    website = models.CharField(max_length=255)
    google_map_url = models.CharField(max_length=255)
    iso = models.ForeignKey(ListingIso, on_delete=models.SET_NULL, null=True)

    contact_person_name = models.CharField(max_length=255)
    contact_person_email = models.CharField(max_length=255)
    contact_person_mobile = models.CharField(max_length=255)

    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    youtube = models.URLField(max_length=255, null=True, blank=True)

    verified = models.CharField(max_length=25, choices=YES_NO_CHOICE)
    supplier = models.CharField(max_length=25, choices=YES_NO_CHOICE)
    distributor = models.CharField(max_length=25, choices=YES_NO_CHOICE)
    manufacturer = models.CharField(max_length=25, choices=YES_NO_CHOICE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

class ListingReviews(models.Model):
    STATUS_CHOICE = [
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,  null=True, blank=True)
    rating = models.PositiveIntegerField(default=5, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICE)

    def __str__(self):
        return self.organization.company_name

class ListingEnquiry(models.Model):
    STATUS_CHOICE = [
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICE)

    def __str__(self):
        return self.organization.company_name

class Advertisements(models.Model):
    STATUS_CHOICE = [
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,  null=True, blank=True)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='Advertisements' ,blank=True, null=True )
    link = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICE)

    def __str__(self):
        return self.organization.company_name



class Insight(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,  null=True, blank=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='insights/', null=True, blank=True)
    description = RichTextField()
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    slug = models.SlugField(max_length=255, unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Insight, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    logo = models.ImageField(upload_to='partners/logos/', null=True, blank=True)  

    def __str__(self):
        return f"Partner Logo {self.id}"