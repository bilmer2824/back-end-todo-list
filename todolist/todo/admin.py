from django.contrib import admin
from .models import Todos
class TodoAdmin(admin.ModelAdmin):
    list_display = ("pk", "todo_title", "todo_data_created", "todo_data_updated", "todo_text", "todo_published")
    pass
admin.site.register(Todos, TodoAdmin)
