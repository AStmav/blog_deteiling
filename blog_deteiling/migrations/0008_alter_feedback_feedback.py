# Generated by Django 4.2.1 on 2023-08-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_deteiling', '0007_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(max_length=400),
        ),
    ]
