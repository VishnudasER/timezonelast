# Generated by Django 5.0 on 2024-02-21 07:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0002_wishlist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(blank=True, max_length=20, null=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('flag', models.BooleanField(default=False)),
                ('discount_type', models.CharField(choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')], default='fixed', max_length=10)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('expire_date', models.DateTimeField()),
                ('coupon_type', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=10)),
                ('min_purchase_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
    ]
