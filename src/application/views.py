from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from src.application.forms import EmployeeForm, TaskForm
from src.application.models import Employee, Task


def dashboard(request):
    return render(request=request, template_name='application/dashboard.html')


def help_view(request):
    return render(request=request, template_name='application/help.html')


# ---------------------------------------------------------------------------------------------------------------------
def employees(request):
    context = {
        'employees': Employee.objects.all()
    }
    return render(request=request, template_name='application/employees.html', context=context)


def employee(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
        context = {
            'employee': emp
        }
        return render(request=request, template_name='application/employee.html')
    except Employee.DoesNotExist:
        messages.error(request=request,
                       message=f"Requested Employee ID: {pk} doesn't exists, please check the employees below.")
        return redirect('application:employees')


def add_employee(request):
    form = None

    if request.method == 'POST':
        form = EmployeeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request=request, message=f'New Employee added successfully')
            return redirect('application:employees', permanent=True)
    else:
        form = EmployeeForm()

    context = {
        'form': form
    }
    return render(request=request, template_name='application/add_employee.html', context=context)


def update_employee(request, pk):
    emp = None
    form = None

    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        messages.error(
            request=request,
            message=f"Requested Employee ID: {pk} doesn't exists, please check the employees below."
        )
        return redirect('application:employees')

    if request.method == 'POST':
        form = EmployeeForm(instance=emp, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request=request, message=f'{emp.first_name} {emp.last_name} details updated successfully')
            return redirect('application:update_employee', emp.pk, permanent=True)
    else:
        form = EmployeeForm(instance=emp)

    context = {
        'form': form
    }
    return render(request=request, template_name='application/add_employee.html', context=context)


def delete_employee(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
        messages.success(request=request, message=f'{emp.first_name} {emp.last_name} deleted successfully')
        emp.delete()
    except Employee.DoesNotExist:
        messages.error(
            request=request,
            message=f"Requested Employee ID: {pk} doesn't exists, please check the employees below."
        )
    return redirect('application:employees')


# ---------------------------------------------------------------------------------------------------------------------

def tasks(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request=request, template_name='application/tasks.html', context=context)


def task(request, pk):
    try:
        tsk = Task.objects.get(pk=pk)
        context = {
            'task': tsk
        }
        return render(request=request, template_name='application/task.html', context=context)
    except Task.DoesNotExist:
        messages.error(request=request,
                       message=f"Requested task ID: {pk} doesn't exists, please check the tasks below.")
        return redirect('application:tasks')


def add_task(request):
    form = None

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request=request, message=f'New task added successfully')
            return redirect('application:tasks', permanent=True)
    else:
        form = TaskForm()

    context = {
        'form': form
    }
    return render(request=request, template_name='application/add_task.html', context=context)


def update_task(request, pk):
    emp = None
    form = None

    try:
        emp = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        messages.error(
            request=request,
            message=f"Requested task ID: {pk} doesn't exists, please check the tasks below."
        )
        return redirect('application:tasks')

    if request.method == 'POST':
        form = TaskForm(instance=emp, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request=request, message=f'{emp.name} details updated successfully')
            return redirect('application:update_task', emp.pk, permanent=True)
    else:
        form = TaskForm(instance=emp)

    context = {'form': form}
    return render(request=request, template_name='application/add_task.html', context=context)


def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        messages.success(request=request, message=f'{task.name} deleted successfully')
        task.delete()
    except Task.DoesNotExist:
        messages.error(
            request=request,
            message=f"Requested task ID: {pk} doesn't exists, please check the tasks below."
        )
    return redirect('application:tasks')
