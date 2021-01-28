from django.shortcuts import render


def dashboard(request):
    return render(request=request, template_name='application/dashboard.html')


# ---------------------------------------------------------------------------------------------------------------------
def employees(request):
    return render(request=request, template_name='application/employees.html')


def employee(request, pk):
    return render(request=request, template_name='application/employee.html')


def add_employee(request):
    return render(request=request, template_name='application/add_employee.html')


def update_employee(request, pk):
    return render(request=request, template_name='application/add_employee.html')


def delete_employee(request, pk):
    return render(request=request, template_name='application/employees.html')


# ---------------------------------------------------------------------------------------------------------------------
def evaluate(request):
    return render(request=request, template_name='application/evaluate.html')


def performance_measures(request):
    return render(request=request, template_name='application/performance_measures.html')


def add_rule(request):
    return render(request=request, template_name='application/add_evaluation_rule.html')


def update_rule(request, pk):
    return render(request=request, template_name='application/add_rule.html')


def delete_rule(request, pk):
    return render(request=request, template_name='application/performance_measures.html')
