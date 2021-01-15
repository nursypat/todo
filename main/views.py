from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("hello nunu")


def test(request):
    return render(request, "test.html")    

def check(request):
    return HttpResponse("teksheruu")

def third(request):
    return render(request, "test3.html")    