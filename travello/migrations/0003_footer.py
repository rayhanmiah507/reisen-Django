# Generated by Django 4.1.5 on 2024-02-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
            ],
        ),
    ]
