from django.http import HttpResponse
from django.shortcuts import render
from staff.models import Employee


def index(request):
    return render(
        request,
        'index.html',
        context={'employees': Employee.objects.all()}
    )
