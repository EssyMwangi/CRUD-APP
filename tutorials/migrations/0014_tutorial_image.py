# Generated by Django 2.1.15 on 2020-06-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0013_remove_tutorial_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
