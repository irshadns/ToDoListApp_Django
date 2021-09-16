from django.contrib import admin
from .models import Task

# Register your models here.


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ['title', 'description', 'complete', 'created', 'user']
