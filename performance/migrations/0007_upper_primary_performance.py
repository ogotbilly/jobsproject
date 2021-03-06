# Generated by Django 2.2.7 on 2020-01-27 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20200124_0822'),
        ('performance', '0006_auto_20200127_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upper_primary_performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('English', models.CharField(max_length=255)),
                ('Kiswahili_or_Kenya_Sign_Language', models.CharField(max_length=255)),
                ('Home_Science', models.CharField(max_length=255)),
                ('Mathematical', models.CharField(max_length=255)),
                ('Agriculture', models.CharField(max_length=255)),
                ('Science_and_Technology', models.CharField(max_length=255)),
                ('Creative_Arts', models.CharField(max_length=255)),
                ('Physical_and_Health_Education', models.CharField(max_length=255)),
                ('Religious_education_activities', models.CharField(max_length=255)),
                ('Social_Studies', models.CharField(max_length=255)),
                ('Teachers_comment', models.TextField()),
                ('Student_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Upper_primary')),
            ],
        ),
    ]
