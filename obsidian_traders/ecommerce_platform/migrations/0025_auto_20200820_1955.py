# Generated by Django 3.0.3 on 2020-08-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_platform', '0024_auto_20200820_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ManyToManyField(to='ecommerce_platform.Coupon'),
        ),
    ]
