from django.shortcuts import render
import subprocess

def insert_temp_data(request):
    if request.method == "GET":
        return render(request, "insert_temp_data.html")

    if request.method == "POST":
        res = request.POST.get("temp_data", None)
        res = res.replace("\r\n", "\n")
        db = request.POST.get("dbname_choice", None)
        dbname = db.split('_')[0]
        dbtype = db.split('_')[1]

        with open("/home/" + dbtype + "/dba/bi/for_insert.sql", "w") as f:
            f.seek(0)
            f.truncate()
            f.write(str(res))

        # print(dbname)
        subprocess.Popen(['nohup', 'su', '-', dbtype, '/home/' + dbtype + '/dba/bi/tmp_' + dbname + '_data.sh'], shell=True, stdout=subprocess.PIPE, start_new_session=True)
    return render(request, 'insert_temp_data.html')
