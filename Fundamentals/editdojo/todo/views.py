from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem #.models from same folder


# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(  request,
                    'todo.html',
                    {'all_items': all_todo_items}
                )

def addTodo(request):
    #create new todo item object and save
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()

    #redirect user to /todo/
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    #create new todo item object and save
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    #redirect user to /todo/
    return HttpResponseRedirect('/todo/')
