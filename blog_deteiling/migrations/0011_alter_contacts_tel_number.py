# Generated by Django 4.2.1 on 2023-08-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_deteiling', '0010_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='tel_number',
            field=models.IntegerField(),
        ),
    ]
