# Generated by Django 3.0.3 on 2020-08-03 15:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce_platform', '0011_remove_userprofile_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='User_Profile',
        ),
    ]
