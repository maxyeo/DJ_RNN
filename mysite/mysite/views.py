from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    return render(request, 'mysite/index.html')