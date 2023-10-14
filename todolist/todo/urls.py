from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', index, name='index'),
    path('id/<int:pk>/', id_list, name="id_list"),
    path('new/', AddTodos.as_view(), name="add_todo"),
    path('todo/<int:pk>/update/', TodoUpdate.as_view(), name="todo_update"),
    path('todo/<int:pk>/delete/', TodoDelete.as_view(), name="todo_delete")
]
