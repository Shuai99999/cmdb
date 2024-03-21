from django.shortcuts import render
from xml.dom.minidom import parse  # 这个用来解析xml文档
from django.shortcuts import render, redirect

xml_file = 'file/mycat_config/server.xml'
doc = parse(xml_file)
root = doc.documentElement
users = root.getElementsByTagName("user")

def refresh_xml():
    xml_file = 'file/mycat_config/test.xml'
    doc = parse(xml_file)
    root = doc.documentElement
    users = root.getElementsByTagName("user")
    xml_file = 'file/mycat_config/server.xml'
    doc = parse(xml_file)
    root = doc.documentElement
    users = root.getElementsByTagName("user")

def mycat_user_list(request):
    xml_file = 'file/mycat_config/server.xml'
    doc = parse(xml_file)
    root = doc.documentElement
    users = root.getElementsByTagName("user")
    user_infos = []
    for user in users:
        user_info = {"username": "", "password": "", "schemas": "", "defaultSchema": "", "readOnly": ""}
        username = user.getAttribute('name')
        user_info["username"] = username
        user_config = user.getElementsByTagName('property')
        for i in range(0, user_config.length):
            attr = user_config.item(i).getAttribute('name')
            value = user_config.item(i).firstChild.data
            user_info[attr] = value
        user_infos.append(user_info)
    return render(request, 'mycat_user_config.html', {'queryset': user_infos})


def mycat_user_add(request):
    if request.method == "GET":
        return render(request, 'mycat_user_add.html')

    form = {"username": "", "password": "", "schemas": "", "defaultSchema": "", "readOnly": ""}
    # if form.is_valid():
    #     form.save()
    # return redirect('/mycat_user_config/mycat_user_list/')
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        schemas = request.POST.get("schemas", None)
        defaultSchema = request.POST.get("defaultSchema", None)
        readOnly = request.POST.get("readOnly", None)
        add_user(username, password, schemas, defaultSchema, readOnly)
        return redirect('/mycat_user_config/mycat_user_list/')

    return render(request, 'mycat_user_add.html', {"form": form})

def mycat_user_edit(request, n_username):
    username = n_username
    if request.method == "GET":
        form = {"username": "", "password": "", "schemas": "", "defaultSchema": "", "readOnly": ""}
        return render(request, 'mycat_user_edit.html', {'form': form})


def mycat_user_delete(request, n_username):

    username = n_username
    drop_user(username)
    return redirect('/mycat_user_config/mycat_user_list/')

def add_user(username, password, schemas, defaultSchema, readOnly):
    add_user = doc.createElement('user')
    root.appendChild(add_user)

    ## 为add_user添加name属性
    nameNode = doc.createAttribute("name")
    add_user.setAttributeNode(nameNode)
    add_user.setAttribute('name', username)

    ## 为add_user添加节点
    userinfoNode = doc.createElement('property')
    userinfoNode.setAttribute('name', 'password')
    userinfoNode.appendChild(doc.createTextNode(password))
    add_user.appendChild(userinfoNode)

    if schemas != "":
        userinfoNode = doc.createElement('property')
        userinfoNode.setAttribute('name', 'schemas')
        userinfoNode.appendChild(doc.createTextNode(schemas))
        add_user.appendChild(userinfoNode)

    if defaultSchema != "":
        userinfoNode = doc.createElement('property')
        userinfoNode.setAttribute('name', 'defaultSchema')
        userinfoNode.appendChild(doc.createTextNode(defaultSchema))
        add_user.appendChild(userinfoNode)

    if readOnly == "true":
        userinfoNode = doc.createElement('property')
        userinfoNode.setAttribute('name', 'readOnly')
        userinfoNode.appendChild(doc.createTextNode(readOnly))
        add_user.appendChild(userinfoNode)

    save_xml(xml_file)

def drop_user(username):
    refresh_xml()
    i = 0
    for user in users:
        name = user.getAttribute('name')
        if username == name:
            to_drop_user = users[i]
            root.removeChild(to_drop_user)
            save_xml(xml_file)
        i += 1

    save_xml(xml_file)

def save_xml(xml_file):
    with open(xml_file, "w", encoding="utf-8") as f:
        doc.writexml(f, indent='', addindent='\t', newl='\n', encoding="utf-8")
    f.close()

    emptyline = '\t\n'
    fb_r = open(xml_file, 'r', encoding="utf-8")
    result = list()
    for line in fb_r.readlines():
        if emptyline in line:
            continue
        elif len(line) == 1:
            continue
        result.append(line)
    finResult = ''.join(result)
    fb_r.close()
    fb_w = open(xml_file, 'w', encoding="utf-8")
    fb_w.write(finResult)
    fb_w.close()