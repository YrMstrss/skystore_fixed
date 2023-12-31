# Generated by Django 4.2.4 on 2023-09-26 19:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_alter_product_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 22, 46, 16, 452867), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 22, 46, 16, 452867), verbose_name='Дата последнего изменения'),
        ),
    ]
