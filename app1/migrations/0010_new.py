# Generated by Django 4.2.6 on 2023-11-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_rename_electric_electric_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('source', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='aks')),
            ],
        ),
    ]
