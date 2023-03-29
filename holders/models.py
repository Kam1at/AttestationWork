from django.db import models
from contacts.models import Contacts
from products.models import Products

NULLABLE = {'blank': True, 'null': True}


class Holders(models.Model):
    FACTORY = 'завод'
    RETAIL_CHAIN = 'розничная сеть'
    SOLE_TRADER = 'индивидуальный предприниматель'
    INSTANCES = (
        (FACTORY, 'завод'),
        (RETAIL_CHAIN, 'розничная сеть'),
        (SOLE_TRADER, 'индивидуальный предприниматель')
    )

    instance = models.CharField(max_length=50, choices=INSTANCES, verbose_name='экземпляр')
    name = models.CharField(max_length=250, verbose_name='название')
    contacts = models.ForeignKey(Contacts, verbose_name='контакты', on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name='продукты')
    supplier = models.ForeignKey("self", verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    indebtedness = models.FloatField(verbose_name='задолженность перед поставщиком', **NULLABLE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звенья'
