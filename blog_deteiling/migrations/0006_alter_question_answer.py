# Generated by Django 4.2.1 on 2023-08-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_deteiling', '0005_alter_feedback_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(default='', max_length=400),
        ),
    ]