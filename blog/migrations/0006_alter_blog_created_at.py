# Generated by Django 4.2.4 on 2023-09-26 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 20, 48, 7, 439540), verbose_name='Дата создания'),
        ),
    ]
