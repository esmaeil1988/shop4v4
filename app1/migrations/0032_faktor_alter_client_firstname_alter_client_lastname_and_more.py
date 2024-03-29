# Generated by Django 4.2.6 on 2023-12-26 18:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='faktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('totalprice', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='firstname',
            field=models.CharField(max_length=20, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastname',
            field=models.CharField(max_length=20, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=20, verbose_name='کلمه عبور'),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=20, verbose_name='نام کاربری'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pprice',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='قیمت قبل از تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت'),
        ),
        migrations.CreateModel(
            name='faktor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnt', models.IntegerField()),
                ('faktor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.faktor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
            ],
        ),
        migrations.AddField(
            model_name='faktor',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client'),
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnt', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
            ],
        ),
    ]
