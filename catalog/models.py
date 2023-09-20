from datetime import datetime

from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    category_description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    unit_price = models.IntegerField(verbose_name='Стоимость')
    creation_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата создания')
    last_change_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')

    version_number = models.IntegerField(default=1, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product} (ver. {self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
