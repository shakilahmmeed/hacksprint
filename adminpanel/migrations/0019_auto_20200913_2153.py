# Generated by Django 3.0.7 on 2020-09-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_merge_20200913_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='track',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
