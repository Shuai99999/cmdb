from django.db import models


# Create your models here.

class ApplicationInfo(models.Model):
    application_id = models.CharField(verbose_name="项目ID", max_length=64)
    application_name = models.CharField(verbose_name="项目名称", max_length=64)
    application_name_short_name = models.CharField(verbose_name="项目简称", max_length=64)
    owner = models.CharField(verbose_name="负责人", max_length=64)
    ops_owner = models.CharField(verbose_name="运维", max_length=64)
    dev_owner = models.CharField(verbose_name="研发", max_length=64)
    test_owner = models.CharField(verbose_name="测试", max_length=64, blank=True)
    application_name_status_choices = (
        (1, "待上线"),
        (2, "在线中"),
        (3, "已下线")
    )
    application_name_status = models.SmallIntegerField(verbose_name="项目状态", choices=application_name_status_choices)
    created_time = models.DateField("创建日期", auto_now_add=True)
    remark = models.TextField(verbose_name="备注", max_length=2000, blank=True)

class IdcInfo(models.Model):
    idc_name = (
        (1, "黄岛电信机房"),
        (2, "浮山路移动机房")
    )
    idc_name = models.SmallIntegerField(verbose_name="数据中心名称", choices=idc_name)
    rack_no = models.CharField(verbose_name="机柜编号", max_length=64)
    rack_power = models.SmallIntegerField(verbose_name="功率（W）")
    rack_current = models.SmallIntegerField(verbose_name="电流（A）*2路")
    monthly_rental = models.DecimalField(verbose_name="月租金", max_digits=10, decimal_places=2)
    rack_status_choices = (
        (1, "在线中"),
        (2, "已下线")
    )
    rack_status = models.SmallIntegerField(verbose_name="机柜状态", choices=rack_status_choices)
    online_date = models.DateField(verbose_name="开通时间")
    remark = models.TextField(verbose_name="备注", max_length=2000, blank=True)

    class Meta:
        unique_together = ('rack_no',)

class MachineInfo(models.Model):
    ip_address = models.CharField(verbose_name="IP地址", max_length=64)
    application_name = models.CharField(verbose_name="项目名称", max_length=64)
    idc_name = models.SmallIntegerField(verbose_name="数据中心名称")
    rack_no = models.CharField(verbose_name="机柜编号", max_length=64)
    cpu_socket = models.SmallIntegerField(verbose_name="CPU颗数")
    cpu_core = models.SmallIntegerField(verbose_name="单个CPU核数")
    ram_socket = models.SmallIntegerField(verbose_name="内存条数")
    ram_size = models.SmallIntegerField(verbose_name="单条内存大小（GB）")
    disk_size = models.SmallIntegerField(verbose_name="磁盘大小（GB）")
    server_type_choices = (
        (1, "物理机"),
        (2, "虚拟机")
    )
    server_type = models.SmallIntegerField(verbose_name="类型", choices=server_type_choices)
    server_purpose_choices = (
        (1, "生产"),
        (2, "测试")
    )
    server_purpose = models.SmallIntegerField(verbose_name="用途", choices=server_purpose_choices)
    server_status_choices = (
        (1, "在线中"),
        (2, "已下线")
    )
    server_status = models.SmallIntegerField(verbose_name="状态", choices=server_status_choices)
    online_date = models.DateField(verbose_name="上架日期")



