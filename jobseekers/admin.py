from django.contrib import admin
from .models import *

# Register your models here.


class JobpersonalAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','birthday', 'created_on', 'status','gender','location','phone_number','nationality')
    list_filter = ("created_on","location")
    search_fields = ['created_on', 'gender','location','firstname']
    # prepopulated_fields = {'slug': ('title',)}

class JobInfoAdmin(admin.ModelAdmin):
    list_display = ('personalinfo','years_of_exprience','highest_qualification', 'cv', 'receive_job_notifation')
    list_filter = ("years_of_exprience","highest_qualification")
    search_fields = ['years_of_exprience', 'highest_qualification']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(JobseekersPersonalIfor,JobpersonalAdmin)

admin.site.register(JobseekersJobinfor,JobInfoAdmin)
