# Generated by Django 3.0.3 on 2020-02-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pre_primary_1_attendance',
            old_name='student_name',
            new_name='student_class',
        ),
        migrations.AlterField(
            model_name='pre_primary_1_attendance',
            name='friday',
            field=models.BooleanField(default=False, verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='pre_primary_1_attendance',
            name='monday',
            field=models.BooleanField(default=False, verbose_name='Mondday'),
        ),
        migrations.AlterField(
            model_name='pre_primary_1_attendance',
            name='thursday',
            field=models.BooleanField(default=False, verbose_name='thursday'),
        ),
        migrations.AlterField(
            model_name='pre_primary_1_attendance',
            name='tuesday',
            field=models.BooleanField(default=False, verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='pre_primary_1_attendance',
            name='wednessday',
            field=models.BooleanField(default=False, verbose_name='Wednessday'),
        ),
    ]
