from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.http import HttpResponseRedirect

from .forms import TodoForm
from .models import Todo


class HomePageView(ListView):
    model = Todo
    template_name = 'todos/home.html'
    context_object_name = "todos"

    http_method_names = ["get", "post"]

    def get_context_data(self, **kwargs):
        context = {**super().get_context_data(**kwargs), 'form': TodoForm(), 'uncompleted_amount': Todo.objects.get_uncompleted_count()}
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")

        todos = (
            Todo.objects.all() if query is None
            else Todo.objects.filter(Q(name__icontains=query) | Q(info__icontains=query))
        )

        return todos

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            
    return redirect_to_request_origin(request)


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()

    return redirect_to_request_origin(request)

def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()

    return redirect_to_request_origin(request)

def redirect_to_request_origin(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

