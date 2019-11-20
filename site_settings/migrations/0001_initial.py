# Generated by Django 2.2.6 on 2019-11-19 14:05

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import site_settings.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Κατάσταση')),
                ('category', models.CharField(choices=[('a', 'Μεγάλο Banner --> (1970*718)'), ('b', 'Μεσαίο Banner --> No Use. For future'), ('c', 'Μικρό Banner -->(600*250)')], default='a', max_length=1)),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Τίτλος')),
                ('text', tinymce.models.HTMLField(blank=True, verbose_name='Σχόλiα')),
                ('image', models.ImageField(upload_to=site_settings.models.upload_banner, validators=[site_settings.models.validate_size])),
                ('url', models.URLField(blank=True, null=True)),
                ('bootstrap_class', models.CharField(default='home-slide', help_text='home-slide text-center', max_length=200)),
            ],
            managers=[
                ('browser', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120, null=True)),
                ('company_address', models.CharField(max_length=200, null=True)),
                ('company_city_zip', models.CharField(max_length=5, null=True)),
                ('company_email', models.EmailField(max_length=254, null=True)),
                ('company_phone', models.CharField(max_length=10, null=True)),
                ('company_fax', models.CharField(max_length=10, null=True)),
                ('logo', models.ImageField(null=True, upload_to='company/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Status')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Ονομασία')),
                ('payment_type', models.CharField(choices=[('a', 'Cash'), ('b', 'Bank'), ('c', 'Credit Card'), ('d', 'Internet Service')], default='a', max_length=1, verbose_name='Είδος')),
                ('site_active', models.BooleanField(default=False, verbose_name='Εμφάνιση στο Site')),
                ('additional_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Μεταφορικά')),
                ('limit_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ελάχιστο Ποσό Χρέωσης')),
                ('first_choice', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Τρόποι Πληρωμής',
            },
        ),
        migrations.CreateModel(
            name='SeoDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('choice', models.CharField(choices=[('a', 'Homepage'), ('b', 'Brands'), ('c', 'New Products'), ('d', 'Offers')], max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Κατάστημα',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Κατάσταση')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Τίτλος')),
                ('additional_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[site_settings.models.validate_positive_decimal], verbose_name='Επιπλέον κόστος')),
                ('limit_value', models.DecimalField(decimal_places=2, default=40, max_digits=6, validators=[site_settings.models.validate_positive_decimal], verbose_name='Μέγιστη Αξία Κόστους')),
                ('first_choice', models.BooleanField(default=False, verbose_name='Πρώτη Επιλογή')),
                ('ordering_by', models.IntegerField(default=1, verbose_name='Priority Order')),
                ('text', tinymce.models.HTMLField(blank=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_settings.Country')),
            ],
            options={
                'verbose_name_plural': 'Τρόποι Μεταφοράς',
                'ordering': ['-ordering_by'],
            },
        ),
    ]
