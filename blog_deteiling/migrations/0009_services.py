# Generated by Django 4.2.1 on 2023-08-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_deteiling', '0008_alter_feedback_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_services', models.CharField(default='', max_length=200)),
                ('price1', models.CharField(default='', max_length=200)),
                ('price2', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
