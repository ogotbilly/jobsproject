# Generated by Django 3.0.3 on 2020-03-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20200310_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pre_primary_1_attendance',
            old_name='student_name',
            new_name='student_class',
        ),
    ]
