# Generated by Django 2.2.7 on 2020-02-14 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20200202_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lower_primary',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must start with 0 if is valid try again!.', regex='[07]\\d{2}\\d{3}\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='lower_primary',
            name='registration_number',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message="Registration number should start with 'L' followed by 4 digits for lower primary otherwise invalid registration number.", regex='[L]\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='lower_primary',
            name='student_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Only characters are allowed for Student name.', regex='^[a-zA-Z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='pre_primary',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must start with 0 if is valid try again!.', regex='[07]\\d{2}\\d{3}\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='pre_primary',
            name='registration_number',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message="Registration number should start with 'P' followed by 4 digits for pre primary otherwise invalid registration number.", regex='[P]\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='pre_primary',
            name='student_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Only characters are allowed for Student name.', regex='^[a-zA-Z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='upper_primary',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must start with 0 if is valid try again!!.', regex='[07]\\d{2}\\d{3}\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='upper_primary',
            name='registration_number',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message="Registration number should start with 'U' followed by 4 digits for upper primary otherwise invalid registration number.", regex='[L]\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='upper_primary',
            name='student_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Only characters are allowed for Student name.', regex='^[a-zA-Z\\s]+$')]),
        ),
    ]
