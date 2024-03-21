from django.shortcuts import render, redirect
from rrswlcmdb import models
from django import forms


# Create your views here.

def idc_list(request):
    queryset = models.IdcInfo.objects.all()

    return render(request, 'idc_list.html', {'queryset': queryset})


class IdcModelForm(forms.ModelForm):
    # 用于增加页面判断，例如用户名长度至少为3
    # name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.IdcInfo
        fields = "__all__"

    # 重新定义这个方法，以后类只要一实例化（form = UserModelForm()）就重新定义这个方法，执行它父类给你的方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环找到所有插件，添加class="form-contrl"
        # for name, field in self.fields.items(): #若前面增加需要用户输入的form以外的字段了，则这里也增加
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
            if name == "online_date":
                field.widget.attrs = {"id": "dt", "class": "form-control", "placeholder": field.label}

def idc_add(request):
    if request.method == "GET":
        form = IdcModelForm()
        return render(request, 'idc_add.html', {"form": form})

    form = IdcModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/idc/list/')

    return render(request, 'idc_add.html', {"form": form})

def idc_edit(request, nid):
    row_object = models.IdcInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        form = IdcModelForm(instance=row_object)
        return render(request, 'idc_edit.html', {'form': form})

    form = IdcModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认是insert，前面加row_object再save就是update了
        form.save()
        return redirect('/idc/list/')
    return render(request, 'idc_edit.html', {"form": form})

def idc_delete(request, nid):
    models.IdcInfo.objects.filter(id=nid).delete()
    return redirect('/idc/list')
