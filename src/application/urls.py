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
    dashboard, help_view,
    employees, add_employee, update_employee, delete_employee, employee,
    tasks, task, add_task, update_task, delete_task, view_login, view_logout,
    report
)

app_name = 'application'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('help/', help_view, name='help'),
    path('accounts/login/', view_login, name='login'),
    path('accounts/logout/', view_logout, name='logout'),

    path('employees/', employees, name='employees'),
    path('employee/<int:pk>/', employee, name='employee'),
    path('add/employee/', add_employee, name='add_employee'),
    path('update/employee/<int:pk>/', update_employee, name='update_employee'),
    path('delete/employee/<int:pk>/', delete_employee, name='delete_employee'),

    path('report/', report, name='report'),

    path('tasks/', tasks, name='tasks'),
    path('task/<int:pk>/', task, name='task'),
    path('add/task/', add_task, name='add_task'),
    path('update/task/<int:pk>/', update_task, name='update_task'),
    path('delete/task/<int:pk>/', delete_task, name='delete_task'),

]
