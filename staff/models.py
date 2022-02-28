from django.db import models


class Employee(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100)
    position = models.CharField('Должность', max_length=100)
    recruitment = models.DateField('Дата приема на работу')
    salary = models.FloatField('Зарплата')
    level = models.IntegerField('Уровень')
    chief = models.ForeignKey(
        'Employee',
        verbose_name='Начальник',
        related_name='subordinates',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
