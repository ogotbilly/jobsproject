# Generated by Django 2.2.7 on 2020-01-27 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0005_lower_primary_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lower_primary_performance',
            name='Student_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Lower_primary'),
        ),
    ]