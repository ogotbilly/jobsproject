# Generated by Django 2.2.7 on 2020-01-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20200124_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lower_primary',
            name='student_class',
            field=models.CharField(choices=[('Grade 3', 'Grade 3'), ('Grade 2', 'Grade 2'), ('Grade 1', 'Grade 1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pre_primary',
            name='student_class',
            field=models.CharField(choices=[('Pre_primary 2', 'Pre_primary 2'), ('Pre_primary 1', 'Pre_primary 1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='upper_primary',
            name='student_class',
            field=models.CharField(choices=[('Grade 6', 'Grade 6'), ('Grade 5', 'Grade 5'), ('Grade 4', 'Grade 4')], max_length=10),
        ),
    ]
