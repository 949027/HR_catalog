from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    name = models.CharField('Фамилия', max_length=200)
    position = models.CharField('Должность', max_length=100)
    recruitment = models.DateField('Дата приема на работу')
    salary = models.FloatField('Зарплата')
    parent = TreeForeignKey(
        'self',
        verbose_name='Начальник',
        related_name='subordinates',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.position} - {self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']
