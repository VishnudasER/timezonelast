# Generated by Django 5.0 on 2024-03-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0015_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banners/')),
            ],
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
    ]
