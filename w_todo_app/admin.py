from django.contrib import admin
from w_todo_app.models import TodoItem, TodoList

admin.site.register(TodoItem)
admin.site.register(TodoList)
