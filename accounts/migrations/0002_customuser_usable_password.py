# Generated by Django 5.1.6 on 2025-02-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='usable_password',
            field=models.BooleanField(default=True),
        ),
    ]
