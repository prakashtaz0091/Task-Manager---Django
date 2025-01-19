from django.contrib import admin
from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'deadline', 'created_at', 'updated_at']
    search_fields = ['name', 'desc']
    list_filter = ['deadline']
