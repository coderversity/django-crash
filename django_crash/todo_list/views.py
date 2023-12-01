from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm
from django.contrib import messages

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo-list.html', { 'todos': todos })

def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'add-task.html', { 'form': form })

def task_detail(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'task-detail.html', { 'task': task })

def delete_task(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted')
        return redirect('todo_list')
    
    return render(request, 'delete-task.html', { 'task': task })