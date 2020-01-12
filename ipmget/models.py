from django.db import models

# Create your models here.


class DNSPools(models.Model):
    """
    DNS资源池表
    """
    dns_name = models.CharField(max_length=64, null=True, verbose_name="dns别名", help_text="dns别名")
    dns_addr = models.CharField(max_length=64, null=True, verbose_name="DNS地址", help_text="DNS地址")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    create_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="创建者", help_text="创建者")
    mod_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="最后修改者", help_text="最后修改者")
    remark = models.TextField(null=True, blank=True, verbose_name="备注", help_text="备注")

    def __str__(self):
        return "{}:{}".format(self.dns_name, self.dns_addr)

    class Meta:
        db_table = "dnspools"
        verbose_name = "DNS资源池表"
        verbose_name_plural = "DNS资源池表"


class IPDHCPools(models.Model):
    """
    IP资源池表
    """
    ip_start = models.CharField(max_length=64, null=True, verbose_name="起始IP地址", help_text="起始IP地址")
    ip_end = models.CharField(max_length=64, null=True, verbose_name="结束IP地址", help_text="结束IP地址")
    ip_mask = models.CharField(max_length=64, default=24, null=True, verbose_name="子网掩码", help_text="子网掩码")
    ip_gateway = models.CharField(max_length=64, null=True, verbose_name="网关", help_text="网关")
    remark = models.TextField(null=True, blank=True, verbose_name="备注", help_text="备注")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    def __str__(self):
        return "{}:{}".format(self.ip_start, self.ip_end, self.ip_gateway)

    class Meta:
        db_table = "dhcppools"
        verbose_name = "IPDHCP表"
        verbose_name_plural = "IPDHCP表"


class IPAddr(models.Model):
    """
    IP表
    """
    ipaddr = models.GenericIPAddressField(verbose_name="IP地址", help_text="IP地址")
    ipuser = models.CharField(max_length=128, null=True, blank=True, verbose_name="IP使用者", help_text="IP使用者")
    ipmac = models.CharField(max_length=128, null=True, blank=True, verbose_name="MAC地址", help_text="MAC地址")
    ip_status_type_choices = (
        ("使用中", "使用者"),
        ("已释放", "已释放"),
        ("未分配", "未分配"),
    )
    ip_status = models.CharField(max_length=8, choices=ip_status_type_choices, blank=True, verbose_name="IP使用状态", help_text="IP使用状态")
    ip_ping = models.CharField(max_length=8, default="down", verbose_name="up网络通畅", help_text="up网络通畅, down网络不可达")
    remark = models.TextField(default="", null=True, blank=True, verbose_name="备注", help_text="备注")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间", help_text="最后更新时间")

    def __str__(self):
        return "{}:{}".format(self.ipaddr, self.ip_status)

    class Meta:
        db_table = "ipaddr"
        verbose_name = "IP资源表"
        verbose_name_plural = "IP资源表"

