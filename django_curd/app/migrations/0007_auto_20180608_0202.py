# Generated by Django 2.0.5 on 2018-06-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180608_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='member_price',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True, verbose_name='会员价'),
        ),
    ]
