from django.db import models


class Contacts(models.Model):
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house = models.CharField(max_length=10, verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'