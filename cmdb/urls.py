"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoapplication.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rrswlcmdb.views import application, idc, insert_temp_data
from rrswlcmdb.views import index
from rrswlcmdb.views import wms_expdata
from rrswlcmdb.views import mycat_user_config
from rrswlcmdb.views import upload_file
from rrswlcmdb.views import re_chdata

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index.index),
    path('application/list/', application.application_list),
    path('application/add/', application.application_add),
    path('application/<int:nid>/edit/', application.application_edit),
    path('application/<int:nid>/delete/', application.application_delete),
    path('idc/list/', idc.idc_list),
    path('idc/add/', idc.idc_add),
    path('idc/<int:nid>/edit/', idc.idc_edit),
    path('idc/<int:nid>/delete/', idc.idc_delete),
    path('wms_expdata/', wms_expdata.wms_expdata),
    path('wms_zx_expdata/', wms_expdata.wms_zx_expdata),
    path('insert_temp_data/', insert_temp_data.insert_temp_data),
    path('mycat_user_config/mycat_user_list/', mycat_user_config.mycat_user_list),
    path('mycat_user_config/mycat_user_add/', mycat_user_config.mycat_user_add),
    path('mycat_user_config/<str:n_username>/edit/', mycat_user_config.mycat_user_edit),
    path('mycat_user_config/<str:n_username>/delete/', mycat_user_config.mycat_user_delete),
    path('upload_file/', upload_file.upload_file),
    path('re_chdata/', re_chdata.re_chdata),
]
