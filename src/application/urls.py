"""emp_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from src.application.views import (
    dashboard, evaluate,
    employees, add_employee, update_employee, delete_employee, employee,
    performance_measures, add_rule, update_rule, delete_rule
)

app_name = 'application'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),

    path('employees/', employees, name='employees'),
    path('employee/<int:pk>/', employee, name='employee'),
    path('add/employee/', add_employee, name='add_employee'),
    path('update/employee/<int:pk>/', update_employee, name='update_employee'),
    path('delete/employee/<int:pk>/', delete_employee, name='delete_employee'),

    path('evaluate/', evaluate, name='evaluate'),
    path('performance_measures/', performance_measures, name='performance_measures'),
    path('add/rule/', add_rule, name='add_rule'),
    path('update/rule/<int:pk>/', update_rule, name='update_rule'),
    path('delete/rule/<int:pk>/', delete_rule, name='delete_rule'),
]
