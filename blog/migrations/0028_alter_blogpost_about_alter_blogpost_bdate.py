# Generated by Django 4.1 on 2022-08-21 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_blogpost_bdate_alter_blogpost_chead0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='about',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 1, 21, 39, 110848)),
        ),
    ]
