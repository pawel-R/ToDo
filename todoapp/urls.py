from django.urls import path
from .views import todoView, addTodo, deleteTodo

urlpatterns = [
    path('todo/', todoView, name='todo-view'),
    path('addTodo/', addTodo, name='add-todo'),
    path('deleteTodo/<int:todo_id>', deleteTodo, name='delete-todo'),
    
]


