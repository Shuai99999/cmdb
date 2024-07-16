from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rrswlcmdb import models
# Create your views here.
import os
import string
import random
import subprocess


def onetime_expdata(request):
    mysql_db_names = ['mysql_cdk_auch_srp_exp', 'mysql_cdk_auch_exp', 'mysql_cdk_nsp_exp', 'mycat_oms_ods_exp',
                      'mycat_oms_otm_exp', 'mysql_oms_cus_st_exp', 'mysql_oms_gtd_st_exp', 'mysql_oms_iop_st_exp',
                      'mysql_oms_iop_st_exp', 'newoms_appoint2_8068_exp', 'newoms_appoint_8068_exp', 'kxbms_exp',
                      'imfs_exp',
                      'mysql_rmdb5722_monitor_exp', 'polardb_cdkread_exp', 'tms_ddzx_aliyun_exp',
                      'mycat_bms8066_ldgdb_exp',
                      'mycat_bms8066_basdb_exp', 'mycat_bms8066_basmidb_exp', 'mycat_bms8066_bizdb_exp',
                      'mycat_bms8066_foudb_exp', 'mycat_bms8066_ldgdb_exp', 'mycat_bms8066_stmdb_exp',
                      'mycat_bms8066_sysdb_exp', 'mycat_htms_exp', 'mysql_kx_exp', 'mysql_ams_exp', 'mysql_xiaohao_exp',
                      'mysql_lejia_read_exp', 'mysql_kx_driver_exp', 'mysql_kx_sc_exp', 'mysql_kx_driver_wide_tab_exp',
                      'rrsmdm_exp', 'mysql_kx_caiwu_exp', 'mysql_kx_az_exp', 'mysql_erp_exp', 'mysql_yunshun_exp',
                      'mysql_kx_zangu_exp', 'mysql_kxpt_exp', 'srm_exp', 'iwms_sysdb_exp', 'iwmsdb_exp', 'gxtms_exp',
                      'daojia_exp', 'xyc_mycat95_exp', 'xyc_mycat95_order_exp', 'crm_mdm_exp', 'crm_exp', 'bmg_gis_exp',
                      'i56_admin_exp']
    oracle_db_names = ['oracle_app_exp', 'oracle_cdk_exp', 'oracle_iwmsa_exp', 'oracle_iwmspf_exp', 'oracle_i1wms_exp',
                       'oracle_i2wms_exp', 'oracle_i3wms_exp', 'oracle_i4wms_exp', 'oracle_wldtm_exp',
                       'oracle_wms7001_exp', 'oracle_tms_exp', 'gps_exp', 'oracle_bms_exp', 'oracle_eam_exp',
                       'oracle_cdkbi_exp', 'oracle_vom2_exp', 'oracle_arch_tms_arch_exp', 'oracle_tms_rac_exp',
                       'oracle_itms_rac_exp', 'saples_exp']

    if request.method == "GET":
        return render(request, "onetime_expdata.html")

    if request.method == "POST":
        filename = request.POST.get("filename", None)
        expdata_db = request.POST.get("expdata_db", None)
        expdata_sql = request.POST.get("expdata_sql", None)
        expdata_sql = expdata_sql.replace("\r\n", "\n")
        if expdata_db in mysql_db_names:
            db_type = 'mysql'
        elif expdata_db in oracle_db_names:
            db_type = 'oracle'
        with open("/home/" + db_type + "/dba/bi/auto_export/" + filename + "_inputs", "w+") as f:
            f.write(str(expdata_sql))
            # f.write(str("\n"))
        subprocess.Popen(
            ['su', '-', db_type, '/home/' + db_type + '/dba/bi/auto_export/add_expdata_job.sh', expdata_db, filename],
            stdout=subprocess.PIPE)
        subprocess.Popen(
            ['su', '-', db_type, '/home/' + db_type + '/dba/bi/auto_export/' + filename + '.sh'],
            stdout=subprocess.PIPE)
        subprocess.Popen(
            ['rm ', '-rf', '/home/' + db_type + '/dba/bi/auto_export/' + filename + '*'],
            stdout=subprocess.PIPE)
        if 'oms' in expdata_db:
            ftpUsername = 'omsexp'
            ftpPassword = '7wS&$M7ffGfLdg93'
        elif 'wms' in expdata_db:
            ftpUsername = 'iwmsexp'
            ftpPassword = 'h$6m$LzBZESvwTcr'
        elif 'cdk' in expdata_db:
            ftpUsername = 'cdkexp'
            ftpPassword = '8UytK6Z*toY5'
        elif 'bms' in expdata_db:
            ftpUsername = 'bmsexp'
            ftpPassword = 'cvh$UhTqVk*eYfHr'
        elif 'app' in expdata_db:
            ftpUsername = 'appexp'
            ftpPassword = 'fDHub0erCGenMpq*'
        elif 'kx' in expdata_db:
            ftpUsername = 'kxexp'
            ftpPassword = 'yRJu*IA$vSTEA$hp'
        elif 'sqm' in expdata_db:
            ftpUsername = 'sqmexp'
            ftpPassword = 'Ya8RNHSk7MO7NIai'
        elif 'tms' in expdata_db:
            ftpUsername = 'tmsexp'
            ftpPassword = 'dSLLg6YLYbRBaFoU'
        elif 'gps' in expdata_db:
            ftpUsername = 'tmsexp'
            ftpPassword = 'dSLLg6YLYbRBaFoU'

        exp_message = '您的数据已导出，请登录rrswl导数ftp，打开文件资源管理器（任意文件夹），输入地址 ftp://10.135.30.96/ 输入 用户名:' + ftpUsername + ' 密码:' + ftpPassword + '，查找文件：' + filename + '.zip，可能有多个同名文件但后缀数字不同，记得变成zip再下载'

    return render(request, 'onetime_expdata.html', {"exp_message": exp_message})
