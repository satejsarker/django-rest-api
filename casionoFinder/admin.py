from django.contrib import admin
from . models import Casino

# Register your models here.
@admin.register(Casino)
class Casinoadmin(admin.ModelAdmin):
    list_display=('id','name','adress','created_at','modified_at')
