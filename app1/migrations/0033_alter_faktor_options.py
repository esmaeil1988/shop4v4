# Generated by Django 4.2.6 on 2023-12-26 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_faktor_alter_client_firstname_alter_client_lastname_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faktor',
            options={'verbose_name': 'فاکتور', 'verbose_name_plural': 'فاکتورها'},
        ),
    ]