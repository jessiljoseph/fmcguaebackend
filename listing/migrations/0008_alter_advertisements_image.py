# Generated by Django 5.1.1 on 2024-10-17 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_country_created_country_updated_state_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Advertisements'),
        ),
    ]
