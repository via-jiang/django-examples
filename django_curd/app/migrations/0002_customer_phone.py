# Generated by Django 2.0.5 on 2018-06-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=15689776543, max_length=11, unique=True, verbose_name='手机'),
            preserve_default=False,
        ),
    ]