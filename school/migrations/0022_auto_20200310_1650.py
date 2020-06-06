# Generated by Django 3.0.3 on 2020-03-10 16:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20200310_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lower_primary',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='invalid phone number, phone number should be in the format of +254', regex='(\\+254)\\s*?(\\d{3})\\s*?(\\d{3})\\s*?(\\d{3})')]),
        ),
        migrations.AlterField(
            model_name='upper_primary',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='invalid phone number, phone number should be in the format of +254', regex='(\\+254)\\s*?(\\d{3})\\s*?(\\d{3})\\s*?(\\d{3})')]),
        ),
    ]