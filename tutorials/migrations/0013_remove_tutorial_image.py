# Generated by Django 2.1.15 on 2020-06-11 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0012_auto_20200611_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='image',
        ),
    ]