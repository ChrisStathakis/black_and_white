# Generated by Django 2.2.6 on 2019-11-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191108_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True),
        ),
    ]
