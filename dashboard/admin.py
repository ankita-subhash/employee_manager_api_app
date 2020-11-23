from django.contrib import admin
from staff.models import EmpInfo, ManagerInfo

class EmpAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    
admin.site.register(EmpInfo, EmpAdmin)
admin.site.register(ManagerInfo)