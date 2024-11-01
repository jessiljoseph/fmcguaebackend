# Generated by Django 5.1.1 on 2024-10-19 09:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
