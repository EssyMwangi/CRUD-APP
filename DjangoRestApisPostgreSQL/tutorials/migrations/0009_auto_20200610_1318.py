# Generated by Django 2.2.6 on 2020-06-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0008_auto_20200610_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='modified_date',
        ),
    ]
