from django.shortcuts import render
from django.http import HttpResponse

def todoView(request):
    return render(request, 'todo.html' )#HttpResponse('hello, this is todoView')

# Create your views here.
