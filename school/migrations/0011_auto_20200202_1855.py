# Generated by Django 2.2.7 on 2020-02-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20200202_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_primary',
            name='student_class',
            field=models.CharField(choices=[('Pre_primary 2', 'Preprimary2'), ('Pre_primary 1', 'Preprimary1')], max_length=10),
        ),
    ]
