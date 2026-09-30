from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

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
    }
]

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def list(request):
    template = loader.get_template('employee_list.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())