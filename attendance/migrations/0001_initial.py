# Generated by Django 3.0.3 on 2020-02-28 07:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0015_auto_20200228_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pre_primary_1_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=True, verbose_name='Mondday')),
                ('tuesday', models.BooleanField(default=True, verbose_name='Tuesday')),
                ('wednessday', models.BooleanField(default=True, verbose_name='Wednessday')),
                ('thursday', models.BooleanField(default=True, verbose_name='thursday')),
                ('friday', models.BooleanField(default=True, verbose_name='Friday')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('student_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Pre_primary')),
            ],
        ),
    ]
