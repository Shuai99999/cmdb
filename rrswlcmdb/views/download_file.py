from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.
import os

def download_files(request):
    files = os.listdir('media/uploads/')
    response = HttpResponse(content_type='application/zip')
    zip_file = FileSystemStorage().zip_folder('media/uploads/', files)
    response['Content-Disposition'] = 'attachment; filename="files.zip"'
    response['Content-Length'] = os.path.getsize(zip_file)
    response.write(open(zip_file, 'rb').read())
    return response