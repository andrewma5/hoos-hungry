# Generated by Django 4.2.6 on 2023-11-13 01:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_menurequest_restaurant_restaurant_menu_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Rating must be at least 1'), django.core.validators.MaxValueValidator(5, message='Rating must be at most 5')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('report_type', models.CharField(choices=[('CL', 'cleanliness'), ('CR', 'crowdedness'), ('FR', 'friendliness'), ('MQ', 'menu quality')], default='CL', max_length=2)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='crowdednessreport',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='crowdednessreport',
            name='user',
        ),
        migrations.RemoveField(
            model_name='friendlinessreport',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='friendlinessreport',
            name='user',
        ),
        migrations.RemoveField(
            model_name='menuqualityreport',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='menuqualityreport',
            name='user',
        ),
        migrations.DeleteModel(
            name='CleanlinessReport',
        ),
        migrations.DeleteModel(
            name='CrowdednessReport',
        ),
        migrations.DeleteModel(
            name='FriendlinessReport',
        ),
        migrations.DeleteModel(
            name='MenuQualityReport',
        ),
    ]
