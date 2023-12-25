from django.shortcuts import render, redirect, reverse
from django.views import View

from todolist_app.models import TodoList


class TodoListView(View):
    def get(self, request):
        todolist = TodoList.objects.all()

        return render(request, 'index.html', context={'todolist': todolist})

    def post(self, request):
        form = request.POST.get('form')
        if form:
            todolist = TodoList.objects.create(TodoItem=form, status=False)
            todolist.save()
        todolist = TodoList.objects.all()
        return render(request, 'index.html', {'todolist': todolist})

def DeleteTodo(request, pk):
    t = TodoList.objects.get(id=pk)
    t.delete()
    return redirect(reverse('home'))


