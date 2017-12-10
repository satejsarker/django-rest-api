from django.contrib import admin
from . models import employees
# Register your models here.
@admin.register(employees)
class employeesDetails(admin.ModelAdmin):
    list_display=('emp_id','first_name','last_name')
