from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import Books


def homepage(request):
   return render(request, "index.html")  


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})    

def check(request):
    return HttpResponse("teksheruu")

def third(request):
    return render(request, "test3.html")    

def books(request):
    books_list = Books.objects.all() 
    return render(request, "books.html", {"books_list": books_list})       