from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

employees = [
    {
        'id': 101,
        'name': 'Rahul',
        'department': 'IT',
        'designation': 'Python Developer'
    },
    {
        'id': 102,
        'name': 'Priya',
        'department': 'HR',
        'designation': 'HR Executive'
    },
    {
        'id': 103,
        'name': 'Amit',
        'department': 'Finance',
        'designation': 'Accountant'
    },
    {
        'id': 104,
        'name': 'Sneha',
        'department': 'Marketing',
        'designation': 'Marketing Executive'
    },
    {
        'id': 105,
        'name': 'Kiran',
        'department': 'IT',
        'designation': 'Django Developer'
    },
    {
        'id': 106,
        'name': 'Tushar',
        'department': 'IT',
        'designation': 'Python Developer'
    }
]


def home(request):
    return render(request, 'home.html')


def list(request):
    context = {
        'employees': employees
    }
    return render(request, 'employee_list.html', context)


def employee_detail(request, id):
    employee = next(
        (employee for employee in employees if employee['id'] == id),
        None
    )
    context = {
        'employee': employee,
        'id': id
    }
    return render(request, 'employee_detail.html', context)


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())