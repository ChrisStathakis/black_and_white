# Generated by Django 2.2.6 on 2020-01-17 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200117_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_favorite',
            field=models.BooleanField(default=False, verbose_name='Προτεριοτητα'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Τιτλος Διευθυνσης'),
        ),
    ]
