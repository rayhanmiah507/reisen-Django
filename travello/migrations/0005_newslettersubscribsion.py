# Generated by Django 4.1.5 on 2024-02-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newslettersubscribsion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
