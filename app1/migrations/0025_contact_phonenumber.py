# Generated by Django 4.2.6 on 2023-12-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_rename_text_contact_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
