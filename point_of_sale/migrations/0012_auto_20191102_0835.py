# Generated by Django 2.2.6 on 2019-11-02 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0011_auto_20191031_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.date(2019, 11, 2), verbose_name='Ημερομηνία'),
        ),
    ]
