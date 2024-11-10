# Generated by Django 5.1.3 on 2024-11-10 18:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(blank=True, default='Dhaka,Bangladesh', max_length=250, null=True)),
                ('profile_picture', models.ImageField(upload_to='profile_pic')),
                ('designation', models.CharField(max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('information', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
