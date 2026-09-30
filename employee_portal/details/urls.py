from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("employees/", views.list, name="list"),
    path("about/", views.about, name="about"),
    path("employees/<int:id>/", views.employee_detail, name="employee_detail"),
]