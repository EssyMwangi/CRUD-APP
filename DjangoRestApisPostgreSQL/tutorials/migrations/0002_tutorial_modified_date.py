# Generated by Django 2.2.6 on 2020-06-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]