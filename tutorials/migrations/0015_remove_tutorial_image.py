# Generated by Django 2.1.15 on 2020-06-11 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0014_tutorial_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='image',
        ),
    ]
