from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    data = {'url' : "https://s3.amazonaws.com/finagicstorage/assets"}
    return render(request, "apple.html",
                         data)