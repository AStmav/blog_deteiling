# Generated by Django 4.2.1 on 2023-08-16 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_deteiling', '0016_remove_post_author_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='images',
        ),
    ]
