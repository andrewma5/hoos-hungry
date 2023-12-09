# Generated by Django 4.2.6 on 2023-11-08 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rejectionmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantrequest',
            name='requester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
