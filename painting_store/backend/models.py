from django.db import models


class Store(models.Model):
    title = models.CharField('paint_name', max_length=50)
    year = models.CharField('create_year', max_length=4)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'

