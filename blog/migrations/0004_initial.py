# Generated by Django 4.1 on 2022-08-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0003_delete_bloges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('head0', models.CharField(max_length=100)),
                ('chead0', models.CharField(max_length=1000)),
                ('head1', models.CharField(max_length=100)),
                ('chead1', models.CharField(max_length=1000)),
                ('head2', models.CharField(max_length=100)),
                ('chead2', models.CharField(max_length=1000)),
                ('head3', models.CharField(max_length=100)),
                ('chead3', models.CharField(max_length=1000)),
            ],
        ),
    ]