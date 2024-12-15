# Generated by Django 5.1.3 on 2024-12-09 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_alter_usermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('restaurant', 'Restaurant'), ('delivery', 'Delivery'), ('courier', 'Courier')], default='user', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('delete', 'Delete'), ('inactive', 'Inactive')], default='active', max_length=20),
        ),
        migrations.CreateModel(
            name='UserLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('address', models.CharField(max_length=255)),
                ('is_default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Location',
                'verbose_name_plural': 'User Locations',
            },
        ),
    ]