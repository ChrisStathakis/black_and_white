# Generated by Django 2.2.6 on 2019-10-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20191031_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributetitle',
            name='default_value',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attributeclass',
            name='is_needed',
            field=models.BooleanField(default=True, verbose_name='Απαιτειται'),
        ),
        migrations.AlterField(
            model_name='attributeclass',
            name='is_radio_button',
            field=models.BooleanField(default=True, verbose_name='Μονη Επιλογη'),
        ),
        migrations.AlterField(
            model_name='attributeclass',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='Τιτλος'),
        ),
    ]
