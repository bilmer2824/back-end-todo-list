from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .forms import TodosForm
from .models import Todos
from django.urls import reverse_lazy, reverse

# Create your views here.


def index(request):
    todolist = Todos.objects.all()
    form = TodosForm()
    context = {
        "todolist": todolist,
        'form': form
    }
    return render(request, "todo/index.html ", context=context)


def id_list(request, pk):
    todolist_id = Todos.objects.filter(pk=pk)
    context = {
        "todolist_id": todolist_id

    }
    return render(request, "todo/index.html ", context=context)


class AddTodos(CreateView):
    form_class = TodosForm
    template_name = 'todo/index.html'
    extra_context = {
        'title': 'class yordamida maqola qowish'
    }
    success_url = reverse_lazy('index')


# def add_todos(request):
#     # if request.method == "POST":
#     form = TodosForm(data=request.POST)
#     if form.is_valid():
#         todos = Todos.objects.create(
#             **form.cleaned_data
#         )
#         todos.save()
#         return redirect('index')


class TodoUpdate(UpdateView):
    model = Todos
    form_class = TodosForm
    # context_object_name = 'todo'
    template_name = 'todo/index.html'
    success_url = reverse_lazy('index')


    # def get_queryset(self):
    #     return Todos.objects.filter(todo_published=True)


class TodoDelete(DeleteView):
    model = Todos
    success_url = reverse_lazy('index')

