from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from . import controller

def index(request):
    if request.method == "GET":
        return render(request, 'home/index.html')
    