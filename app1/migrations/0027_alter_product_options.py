# Generated by Django 4.2.6 on 2023-12-12 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_alter_category_title_alter_contact_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
    ]
