# Generated by Django 3.0.7 on 2020-07-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_auto_20200727_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='default_selected',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
