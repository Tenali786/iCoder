# Generated by Django 4.1 on 2022-08-28 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_remove_blogpost_content_blogpost_about_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2022, 8, 28, 17, 18, 10, 97029)),
        ),
    ]