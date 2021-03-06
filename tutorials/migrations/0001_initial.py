# Generated by Django 3.0.7 on 2020-06-12 06:55

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('published_status', models.BooleanField(default=False)),
                ('content', models.TextField(default='', max_length=500)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('photo', pyuploadcare.dj.models.ImageField()),
            ],
        ),
    ]
