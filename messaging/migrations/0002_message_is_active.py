# Generated by Django 3.0.3 on 2020-03-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]