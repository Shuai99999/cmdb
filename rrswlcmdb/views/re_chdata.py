from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rrswlcmdb import models
# Create your views here.
import os
import string
import random
import subprocess
import requests
import json
import os
import sys

def re_chdata(request):
    if request.method=="GET":
        return render(request, "re_chdata.html")

    if request.method=="POST":
        reFLWID = request.POST.get("FLWID", None)

        credential = "eyJzdWJqZWN0IjoiMDE0NTQyMjEiLCJwYXNzd29yZCI6ImQybHVaRzkzYzBBeE1nPT0iLCJ0eXBlIjoxfQ%3D%3D"
        iam_token_url = "https://iama.haier.net/api/oauth/authorize?client_id=cb3b02710dd7ebd0b10762405121d418&credential=" + credential + "&loginType=2&redirect_uri=https%3A%2F%2Frrsoa.rrswl.com%2Fuuc.html%3F%24%24query%24%24eyJyZWRpcmVjdCI6ImluZGV4In0%40%40%24%24end%24%24"
        iam_token_payload = {}
        iam_token_headers = {
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'languageEnv': 'cn',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json, text/plain, */*',
            'Application-Key': 'cb3b02710dd7ebd0b10762405121d418',
            'sec-ch-ua-platform': '"Windows"',
            'host': 'iama.haier.net'
        }

        iam_token_get = requests.get(iam_token_url, headers=iam_token_headers, data=iam_token_payload)

        iam_token = json.loads(iam_token_get.text)

        iam_token = iam_token.get('data').get('access_token')

        token_url = "https://rrsoa.rrswl.com/uniedp-web/open/api/authLogin/authToken"

        token_payload = json.dumps({
            "accessToken": iam_token
        })

        token_headers = {
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"'
        }

        task_token = requests.request("POST", token_url, headers=token_headers, data=token_payload)

        task_token = json.loads(task_token.text)

        task_token = task_token.get('data').get('token')

        headers = {
            'Host': 'rrsoa.rrswl.com',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Connection': 'keep-alive',
            'Content-Type': "application/json",
            'Referer': 'https://rrsoa.rrswl.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            'Token': task_token,
        }

        url = 'https://rrsoa.rrswl.com/uniedp-web/oa/flowable/processInst/page?order=desc&orderField=endTime,createDate&sumFields=&page=1&limit=500&source=done-1&formCode=&formName=&procTitle=&procName=&beginDateStr=&endDateStr=&status=&startBy='
        done_list_url = requests.get(url=url, headers=headers)

        done_list = json.loads(done_list_url.text)

        # print(done_list)

        task_url = "https://rrsoa.rrswl.com/uniedp-web/oa/flowable/processInst/instFormInfo?instId=1737755866406129665&taskId=b8bf87fb-9fde-11ee-8d66-00505693bc47&monitor=false&ccFlag=false"
        for i in done_list.get('data').get('list'):
            # print(i)
            instId = i.get('id')
            # print(instId)
            taskId = i.get('procInstId')
            # print(taskId)
            flwId = i.get('procBizCode')
            # print(flwId)
            # if flwId == "FLW20240201076289":
            if flwId == reFLWID:
                fwl_url = "https://rrsoa.rrswl.com/uniedp-web/oa/flowable/processInst/instFormInfo?instId=" + instId + "&taskId=" + taskId + "&monitor=false&ccFlag=false"
                payload = {}
                fwl_response = requests.request("GET", fwl_url, headers=headers, data=payload)
                # print(fwl_response.text)
                task_details = json.loads(fwl_response.text)
                task_detail = json.loads(task_details.get('data').get('boData'))
                fileId = task_detail.get('fileId')
                db_name = task_detail["databaseAddress"]

                if 'cdk' in db_name and 'mysql' not in db_name:
                    db = 'cdk_pr'
                elif 'rckdb' in db_name:
                    db = 'cdk_pr'
                elif 'sqm' in db_name:
                    db = 'sqm_pr'
                elif 'iwmspf' in db_name:
                    db = 'iwmspf_pr'
                elif 'i1wms' in db_name:
                    db = 'i1wms_pr'
                elif 'i2wms' in db_name:
                    db = 'i2wms_pr'
                elif 'i3wms' in db_name:
                    db = 'i3wms_pr'
                elif 'rrslesdb' in db_name:
                    db = 'i2wms_pr'
                elif 'rrswldb' in db_name:
                    db = 'i1wms_pr'
                elif 'wloms2' in db_name:
                    db = 'oms2_pr'
                elif 'wloms1' in db_name:
                    db = 'oms1_pr'
                elif '10.133.28.7' in db_name:
                    db = 'tms_pr'
                elif '10.135.17.94' in db_name:
                    db = 'app_pr'
                elif 'iwmsa' in db_name:
                    db = 'iwmsa_pr'
                elif 'huyi' in db_name:
                    db = 'huyi'
                elif 'kuajing' in db_name:
                    db = 'haierkuajing'
                else:
                    db = ''

                if db:
                    if fileId:
                        fileIdArray = fileId.split(',')
                        for fileIdArrayItem in fileIdArray:
                            # print(fileIdArrayItem)

                            attach_url = 'https://rrsoa.rrswl.com/uniedp-web/obs/download?ossId=' + fileIdArrayItem + '&token=' + task_token + '&charset=UTF-8'

                            attach = requests.get(attach_url)

                            with open('/home/oracle/dba/prod/input', "wb") as code:
                                code.write(attach.content)

                    else:
                        sql_text = task_detail["applyRemark"]
                        sql_text = sql_text.encode()
                        with open('/home/oracle/dba/prod/input', "wb") as code:
                            code.write(sql_text)

    # subprocess.Popen(['su', '-', 'oracle', '/home/oracle/dba/prod/chdata.sh', db], stdout=subprocess.PIPE)
    p = subprocess.Popen(['su', '-', 'oracle', '/home/oracle/dba/prod/chdata.sh', db], stdout=subprocess.PIPE)
    # p = subprocess.run(['su', '-', 'oracle', '/home/oracle/dba/prod/chdata.sh', db], capture_output = True, stdout=subprocess.PIPE).decode('utf-8')
    chdata_result = p.stdout
    return render(request, 're_chdata.html', {"chdata_result": chdata_result})

