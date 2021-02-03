from django.contrib import admin
from .models import Employee, Task, RegularReport, RegularReportStats


admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(RegularReport)
admin.site.register(RegularReportStats)


admin.site.site_header = 'EMS System (ROOT ACCESS)'
admin.site.index_title = 'Dashboard'
admin.site.site_title = 'Developer'