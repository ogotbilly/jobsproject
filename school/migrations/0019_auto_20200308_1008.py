# Generated by Django 3.0.3 on 2020-03-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0018_auto_20200308_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='image',
            field=models.ImageField(default='school.jpg', upload_to='profile_pics'),
        ),
    ]
