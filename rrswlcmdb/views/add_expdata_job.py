from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rrswlcmdb import models
# Create your views here.
import os
import string
import random
import subprocess

def add_expdata_job(request):
    if request.method=="GET":
        return render(request, "add_expdata_job.html")

    if request.method=="POST":
        expdata_crontab = request.POST.get("expdata_crontab", None)
        filename = request.POST.get("filename", None)
        expdata_db = request.POST.get("expdata_db", None)
        expdata_sql = request.POST.get("expdata_sql", None)
        expdata_sql = expdata_sql.replace("\r\n", "\n")
        with open("/home/mysql/dba/bi/auto_export/" + filename + "_input", "w") as f:
            f.write(str(expdata_sql))
            # f.write(str("\n"))
    subprocess.Popen(['su', '-', 'mysql', '/home/mysql/dba/bi/auto_export/add_expdata_job.sh', expdata_db, filename], stdout=subprocess.PIPE)
    return render(request, 'add_expdata_job.html')