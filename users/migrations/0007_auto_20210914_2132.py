# Generated by Django 3.2.7 on 2021-09-14 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pusblisher',
            name='category_ar',
        ),
        migrations.RemoveField(
            model_name='pusblisher',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='pusblisher',
            name='category_fr',
        ),
        migrations.AddField(
            model_name='pusblisher',
            name='category',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='pusblisher',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pusblisher',
            name='send',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pusblisher',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
