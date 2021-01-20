from django.shortcuts import render, HttpResponse, redirect
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


def add_todo(request):
        form = request.POST
        text = form["todo_text"]
        todo = ToDo(text = text)
        todo.save()
        return redirect(test)  



def add_book(request):
        form = request.POST
        title1 = form["title_text"]
        price1 = form["price_text"]
        subtitle1 = form["sustitle_text"]
        description1 = form["description_text"]
        genre1 = form["genre_text"]
        author1 = form["author_text"]
        year1 = form["year_text"] 
        book =  Books(
            title =  title1,
            price = price1, 
            subtitle = subtitle1,
            description = description1, 
            genre = genre1, 
            author = author1, 
            year = year1 ) 

        book.save()
        return redirect(books)  

def delete_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.delete()
    return redirect(test)  


def mark_todo(request, id):
    todo= ToDo.objects.get(id = id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo= ToDo.objects.get(id = id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)
