# Generated by Django 3.0.3 on 2020-03-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_auto_20200304_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twiliomesaage',
            name='Price',
        ),
    ]
