# Generated by Django 5.1.3 on 2024-11-23 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='service',
        ),
    ]