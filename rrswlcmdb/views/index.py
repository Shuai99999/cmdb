from django.shortcuts import render, redirect
from rrswlcmdb import models
# Create your views here.

def index(request):

    return render(request, 'index.html')
