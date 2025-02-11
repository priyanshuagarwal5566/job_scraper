from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary')
    search_fields = ('title', 'company', 'location')

admin.site.register(Job, JobAdmin)
