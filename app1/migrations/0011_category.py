# Generated by Django 4.2.6 on 2023-11-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
