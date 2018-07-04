# Generated by Django 2.0.5 on 2018-07-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=24, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('count', models.IntegerField(verbose_name='总数')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer', verbose_name='客户')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=24, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=28, max_digits=40, verbose_name='零售价')),
                ('member_price', models.DecimalField(blank=True, decimal_places=28, max_digits=40, null=True, verbose_name='会员价')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=120, verbose_name='供应商')),
                ('address', models.CharField(max_length=512, verbose_name='地址')),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=24, verbose_name='标签')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Supplier', verbose_name='供应商'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(through='app.Order', to='app.Product'),
        ),
    ]
