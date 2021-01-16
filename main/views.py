from django.shortcuts import render, HttpResponse

def homepage(request):
   return render(request, "index.html")  


def test(request):
    return render(request, "test.html")    

def check(request):
    return HttpResponse("teksheruu")

def third(request):
    return render(request, "test3.html")    