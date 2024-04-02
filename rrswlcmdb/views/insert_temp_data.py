from django.shortcuts import render
import subprocess

def insert_temp_data(request):
    if request.method == "GET":
        return render(request, "insert_temp_data.html")

    if request.method == "POST":
        res = request.POST.get("temp_data", None)
        res = res.replace("\r\n", "\n")
        with open("/home/oracle/dba/bi/for_insert.sql", "w") as f:
            f.seek(0)
            f.truncate()
            f.write(str(res))
        dbname = request.POST.get("dbname_choice", None)
        print(dbname)
    subprocess.Popen(['su', '-', 'oracle', '/home/oracle/dba/bi/tmp_' + dbname + '_data.sh'], stdout=subprocess.PIPE)
    return render(request, 'insert_temp_data.html')
