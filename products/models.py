from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    model = models.CharField(max_length=250, verbose_name='модель')
    date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
