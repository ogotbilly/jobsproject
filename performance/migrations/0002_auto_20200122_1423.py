# Generated by Django 2.2.7 on 2020-01-22 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_upper_primary'),
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pre_primary_performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language_activities', models.CharField(max_length=255)),
                ('Mathematical_activities', models.CharField(max_length=255)),
                ('Environmental_ctivities', models.CharField(max_length=255)),
                ('Psychomotor_and_creative_activities', models.CharField(max_length=255)),
                ('Religious_education_activities', models.CharField(max_length=255)),
                ('Teachers_comment', models.TextField()),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Pre_primary')),
            ],
        ),
        migrations.DeleteModel(
            name='Lower_primary_performance',
        ),
    ]
