from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.
def content(request):
    return render(request, "content.html")
