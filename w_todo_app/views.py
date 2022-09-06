from django.views.generic import ListView
from .models import TodoList, TodoItem

class ListListView(ListView):
    model = TodoList
    template_name = "w_todo_app/index.html"

class ItemListView(ListView):
    model = TodoItem
    template_name = "w_todo_app/todo_list.html"

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = TodoList.objects.get(id=self.kwargs["list_id"])
        return context

