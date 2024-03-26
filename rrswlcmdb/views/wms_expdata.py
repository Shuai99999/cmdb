from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rrswlcmdb import models
# Create your views here.
import os
import string
import random
import subprocess

def wms_expdata(request):
    if request.method=="GET":
        return render(request, "wms_expdata.html")

    if request.method=="POST":
        res = request.POST.get("wms_expsql", None)
        res = res.replace("\r\n", "\n")
        with open("/home/oracle/dba/bi/wms_input", "w") as f:
            f.write(str(res))
            # f.write(str("\n"))
        number_of_strings = 5
        length_of_string = 8
        for x in range(number_of_strings):
            filename=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
        exp_message='您的数据已导出，请登录rrswl导数ftp，打开文件资源管理器（任意文件夹），输入地址 ftp://10.135.30.96/ 输入 用户名:iwmsexp 密码:h$6m$LzBZESvwTcr，查找文件：'+ filename +'_i1wms.zip '+ filename +'_i2wms.zip '+ filename +'_iwmsa.zip'
        # print(exp_message)
    subprocess.Popen(['su', '-', 'oracle', '/home/oracle/dba/bi/wms_for_exp.sh', filename], stdout=subprocess.PIPE)
    return render(request, 'wms_expdata.html', {"exp_message": exp_message})


def wms_zx_expdata(request):
    if request.method=="GET":
        return render(request, "wms_zx_expdata.html")

    if request.method=="POST":
        zx = request.POST.get("wms_exp_zx", None)
        zx = zx.replace("\r\n", "\n")
        with open("/home/oracle/dba/bi/wms_zx_whcode", "w") as f:
            f.write(str(zx))

        sql = request.POST.get("wms_expsql", None)
        sql = sql.replace("\r\n", "\n")
        with open("/home/oracle/dba/bi/wms_input", "w") as f:
            f.write(str(sql))

        number_of_strings = 5
        length_of_string = 8
        for x in range(number_of_strings):
            filename=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
        exp_message='您的数据已导出，请登录rrswl导数ftp，打开文件资源管理器（任意文件夹），输入地址 ftp://10.135.30.96/ 输入 用户名:iwmsexp 密码:h$6m$LzBZESvwTcr，查找文件：'+ filename +'_i1wms.zip '+ filename +'_i2wms.zip '+ filename +'_iwmsa.zip'
        # print(exp_message)
    subprocess.Popen(['su', '-', 'oracle', '/home/oracle/dba/bi/wms_for_whcode_exp_union.sh', filename], stdout=subprocess.PIPE)
    return render(request, 'wms_zx_expdata.html', {"exp_message": exp_message})

