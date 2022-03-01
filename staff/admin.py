from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Employee


class EmployeeAdmin(DjangoMpttAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
