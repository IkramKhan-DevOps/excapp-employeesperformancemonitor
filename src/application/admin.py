from django.contrib import admin
from .models import Employee, Task


admin.site.register(Employee)
admin.site.register(Task)


admin.site.site_header = 'EMS System'
admin.site.index_title = 'Dashboard'
admin.site.site_title = 'Developer'