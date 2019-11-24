# Generated by Django 2.2.6 on 2019-11-22 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20191121_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributerelated',
            name='action_related',
            field=models.CharField(choices=[('HIDE', 'Hide')], max_length=20, verbose_name='Πακετο'),
        ),
        migrations.AlterField(
            model_name='attributerelated',
            name='attribute_related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_related', to='catalogue.AttributeClass', verbose_name='Παραλήπτησ'),
        ),
        migrations.AlterField(
            model_name='attributerelated',
            name='attribute_selected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_selected', to='catalogue.AttributeClass', verbose_name='Αποστολεας'),
        ),
    ]
