# Generated by Django 4.2.6 on 2023-11-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_special_product_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='electric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('tozih', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='aks')),
            ],
        ),
    ]