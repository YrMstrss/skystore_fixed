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
