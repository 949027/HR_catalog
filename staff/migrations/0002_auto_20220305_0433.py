import random
from django.db import migrations
from faker import Faker
from django_seed import Seed

from staff.models import Employee


fake = Faker('Ru_ru')
seeder = Seed.seeder()


def add_employee(amount, position, chief_level):
    for chief in Employee.objects.filter(level=chief_level):
        seeder.add_entity(Employee, amount, {
            'name': lambda x: fake.name(),
            'level': chief_level + 1,
            'position': position,
            'recruitment': lambda x: seeder.faker.date(),
            'salary': lambda x: random.randint(20000, 100000),
            'parent': chief,
        })
        seeder.execute()


def fill_db(apps, schema_editor):
    Employee.objects.create(
        name=fake.name(),
        position='Генеральный директор',
        recruitment=fake.date(),
        salary=random.randint(20000, 100000),
        parent=None,
    )

    add_employee(
        chief_level=0,
        position='Директор департамента',
        amount=15,
    )
    add_employee(
        chief_level=1,
        position='Начальник отдела',
        amount=15,
    )
    add_employee(
        chief_level=2,
        position='Руководитель группы',
        amount=15,
    )
    add_employee(
        chief_level=3,
        position='Специалист',
        amount=15,
    )
    Employee.objects.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_db),
    ]
