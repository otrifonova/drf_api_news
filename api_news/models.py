from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Тип')
    color = models.CharField(max_length=20, db_index=True, verbose_name='Цвет')

    class Meta:
        verbose_name_plural = 'Типы новостей'
        verbose_name = 'Тип'
        ordering = ['id']

    def __str__(self):
        return self.name


class News(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип новости')
    name = models.CharField(max_length=100, verbose_name="Имя")
    summary = models.TextField(verbose_name="Краткое описание")
    text = models.TextField(verbose_name="Полное описание")

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-id']
