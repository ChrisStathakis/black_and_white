# Generated by Django 2.2.6 on 2020-05-17 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0008_auto_20200118_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.date(2020, 5, 17), verbose_name='Ημερομηνία'),
        ),
    ]
