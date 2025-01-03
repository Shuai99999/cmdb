# Generated by Django 3.2.16 on 2023-01-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(max_length=64, verbose_name='项目ID')),
                ('application_name', models.CharField(max_length=64, verbose_name='项目名称')),
                ('application_name_short_name', models.CharField(max_length=64, verbose_name='项目简称')),
                ('owner', models.CharField(max_length=64, verbose_name='负责人')),
                ('ops_owner', models.CharField(max_length=64, verbose_name='运维')),
                ('dev_owner', models.CharField(max_length=64, verbose_name='研发')),
                ('test_owner', models.CharField(blank=True, max_length=64, verbose_name='测试')),
                ('application_name_status', models.SmallIntegerField(choices=[(1, '待上线'), (2, '在线中'), (3, '已下线')], verbose_name='项目状态')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('remark', models.TextField(blank=True, max_length=2000, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='IdcInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idc_name', models.SmallIntegerField(choices=[(1, '黄岛电信机房'), (2, '浮山路移动机房')], verbose_name='数据中心名称')),
                ('rack_no', models.CharField(max_length=64, verbose_name='机柜编号')),
                ('rack_power', models.SmallIntegerField(verbose_name='功率（W）')),
                ('rack_current', models.SmallIntegerField(verbose_name='电流（A）*2路')),
                ('monthly_rental', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='月租金')),
                ('rack_status', models.SmallIntegerField(choices=[(1, '在线中'), (2, '已下线')], verbose_name='机柜状态')),
                ('online_date', models.DateField(verbose_name='开通时间')),
                ('remark', models.TextField(blank=True, max_length=2000, verbose_name='备注')),
            ],
            options={
                'unique_together': {('rack_no',)},
            },
        ),
    ]
