from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rrswlcmdb import models
# Create your views here.
import os

def wms_expdata(request):

    return render(request, 'upload_file.html')

def upload_file(request):
    if request.method=="GET":
        return render(request, "upload_file.html")

    if request.method=="POST":
        myFile = request.FILES.get("myfile", None)
        if myFile:
            path='media/uploads/'
            if not os.path.exists(path):
                os.makedirs(path)
            dest = open(os.path.join(path+myFile.name), 'wb+')
            for chunk in myFile.chunks():
                dest.write(chunk)
            messages.success(request, '上传完成！')
            return redirect('/upload_file/')
        else:
            messages.success(request, '没有上传文件！')
            return redirect('/upload_file/')
