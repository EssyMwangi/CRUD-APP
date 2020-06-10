# Generated by Django 2.2.6 on 2020-06-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20200610_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='content',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
