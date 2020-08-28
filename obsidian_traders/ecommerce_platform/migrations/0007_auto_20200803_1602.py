# Generated by Django 3.0.3 on 2020-08-03 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce_platform', '0006_auto_20200731_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(default='', max_length=20)),
                ('postal_code', models.IntegerField(max_length=7, null=True)),
                ('city', models.CharField(default='', max_length=14)),
                ('country', models.CharField(default='', max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('SMARTPHONES', 'SMARTPHONES'), ('CLOTHING', 'CLOTHING'), ('HOME APPLIANCES', 'HOME APPLIANCES'), ('COMPUTING', 'COMPUTING')], default='', help_text='Product Category', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/none/no-image.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('gender', models.CharField(default='', max_length=8)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ecommerce_platform.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
