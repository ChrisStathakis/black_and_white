# Generated by Django 2.2.6 on 2020-01-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0005_auto_20191124_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='category',
            field=models.CharField(choices=[('c', 'Μηνες'), ('b', 'Εβδομαδες'), ('a', 'Μέρες')], max_length=1, verbose_name='Κατηγορία'),
        ),
    ]
