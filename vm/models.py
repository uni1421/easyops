from django.db import models


# Create your models here.


class VCenter(models.Model):
    """
    Vcenter表
    """
    vc_name = models.CharField(max_length=128, verbose_name="Vcenter/esxi name", help_text="Vcenter或esxi名称、别名")
    vc_ip = models.GenericIPAddressField(unique=True, verbose_name="Vcenter/Esxi管理IP", help_text="Vcenter/Esxi管理IP")
    vc_user = models.CharField(max_length=32, verbose_name="Vcenter/Esxi管理用户", help_text="Vcenter/Esxi管理用户")
    vc_pwd = models.CharField(max_length=128, verbose_name="Vcenter/Esxi管理密码", help_text="Vcenter/Esxi管理密码")
    vc_port = models.CharField(max_length=8, default=443, verbose_name="Vcenter远程管理端口", help_text="Vcenter远程管理端口")
    vc_sync_status = models.CharField(max_length=128, null=True, blank=True, verbose_name="最后一次同步数据时间")
    vc_created_time = models.DateTimeField(auto_now_add=True, verbose_name="加入管理时间", help_text="加入管理时间")

    class Meta:
        db_table = "vcenter"
        verbose_name = "vcenter/esxi表"
        verbose_name_plural = "vcenter/esxi表"

    def __str__(self):
        return self.vc_ip


class EsxiHosts(models.Model):
    """
    esxi物理主机表
    """
    name = models.CharField(max_length=128, null=True, verbose_name="esxi物理主机别名", help_text="esxi物理主机别名")
    vendor = models.CharField(max_length=128, null=True, verbose_name="厂商", help_text="厂商")
    model = models.CharField(max_length=128, null=True, verbose_name="型号", help_text="型号")
    sn = models.CharField(max_length=128, null=True, verbose_name="SN", help_text="sn")
    uuid = models.CharField(max_length=128, null=True, verbose_name="uuid", help_text="uuid")
    fullname = models.CharField(max_length=128, null=True, verbose_name="系统", help_text="fullname")
    numcpupkgs = models.CharField(max_length=128, null=True, verbose_name="CPU插槽")
    numcpucores = models.CharField(max_length=128, null=True, verbose_name="每个插槽内核数")
    numcputhreads = models.CharField(max_length=128, null=True, verbose_name="逻辑处理器个数")
    cpumhz = models.CharField(max_length=128, null=True, verbose_name="CPU频率")
    cpumodel = models.CharField(max_length=128, null=True, verbose_name="CPU型号")
    cpuusage = models.CharField(max_length=128, null=True, verbose_name="CPU使用率")
    memorytotal = models.CharField(max_length=128, null=True, verbose_name="memorySize总内存量(MB)")
    memorysize = models.CharField(max_length=128, null=True, verbose_name="可用内存(MB)")
    overallmemory = models.CharField(max_length=128, null=True, verbose_name="内存使用率")
    powerstate = models.CharField(max_length=64, null=True, verbose_name="主机状态")
    uptime = models.CharField(max_length=128, null=True, verbose_name="正常运行时间")
    boottime = models.CharField(max_length=128, null=True, verbose_name="boottime")
    ipaddress = models.GenericIPAddressField(unique=True, null=True, verbose_name="远程管理IP")
    port = models.CharField(max_length=8, default=443, null=True, blank=True, verbose_name="远程管理端口")
    vmnum = models.IntegerField(null=True, verbose_name="虚拟机数量")
    datastorenum = models.IntegerField(null=True, verbose_name="存储数量")

    class Meta:
        db_table = "esxihosts"
        verbose_name = "esxi物理主机表"
        verbose_name_plural = "esxi物理主机表"

    def __str__(self):
        return self.ipaddress


class VMHosts(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')
    instanceuuid = models.CharField(max_length=128, verbose_name='instanceUuid')
    uuid = models.CharField(max_length=128, verbose_name='uuid')
    vmpathname = models.CharField(max_length=128, verbose_name='vmPathName')
    numcpu = models.CharField(max_length=128, verbose_name='numCpu')
    guestid = models.CharField(max_length=128, verbose_name='guestId')
    guestfullname = models.CharField(max_length=128, verbose_name='guestFullName')
    powerstate = models.CharField(max_length=128, null=True, verbose_name='powerState')
    ipaddress = models.CharField(max_length=128, null=True, verbose_name='ipAddress')
    memorysizemb = models.CharField(max_length=128, null=True, verbose_name='memorySizeMB')
    esxi_id = models.ForeignKey(EsxiHosts, null=True, default='', on_delete=models.SET_NULL)
    dc_name = models.CharField(null=True, max_length=128, verbose_name='datacenter name')
    dc_moid = models.CharField(null=True, max_length=128, verbose_name="datacenter moid")
    moid = models.CharField(null=True, max_length=128, verbose_name="moId")
    template = models.CharField(null=True, max_length=16, verbose_name="该虚拟机是否是模板机 true/false")

    def __str__(self):
        return self.ipaddress

    class Meta:
        db_table = "vmhosts"
        verbose_name = "虚拟机清单表"
        verbose_name_plural = "虚拟机清单表"


