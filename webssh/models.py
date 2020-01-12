from django.db import models

# Create your models here.


class HostRemoteAuth(models.Model):

    auth_type_choices = (
        ("password", "password"),
        ("ssh-key", "ssh-key"),
    )
    username = models.CharField(max_length=32, verbose_name="用户名", help_text="用户名")
    password = models.CharField(max_length=256, null=True, blank=True, verbose_name="密码")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "主机认证表"
        verbose_name_plural = "主机认证表"


class HostRemote(models.Model):
    host = models.ForeignKey(to="vm.VMHosts", verbose_name="管理虚拟机")
    remoteauth = models.ForeignKey(to="HostRemoteAuth", verbose_name="主机认证方式")

    def __str__(self):
        return "{}:{}".format(self.host, self.remoteauth)

    class Meta:
        verbose_name = ""
        verbose_name_plural = ""


class HostGroup(models.Model):
    """
    主机组表
    """
    groupname = models.CharField(max_length=64, unique=True, verbose_name="主机组名称", help_text="主机组名称")
    hostremote = models.ManyToManyField(to="HostRemote")

    class Meta:
        verbose_name = "主机组表"
        verbose_name_plural = "主机组表"


class SShLogs(models.Model):
    LOGIN_CHOICES = (
        ('web', 'web'),
        ('ssh', 'ssh')
    )
    user = models.CharField(max_length=16, null=True, verbose_name='登录用户')
    host = models.CharField(max_length=128, null=True, verbose_name='登录主机')
    remote_ip = models.CharField(max_length=16, verbose_name='来源IP')
    login_type = models.CharField(max_length=8, choices=LOGIN_CHOICES, default='web', verbose_name='登录方式')
    start_time = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='登录时间')
    end_time = models.DateTimeField(null=True, verbose_name='结束时间')
    hour_longtime = models.CharField(max_length=256, null=True, blank=True, verbose_name='登录时长')

    class Meta:
        verbose_name = "ssh审计日志"
        verbose_name_plural = "ssh审计日志"


class RecorderLog(models.Model):
    """
    存储审计回放
    """
    log = models.ForeignKey(to="SShLogs", null=True, blank=True, on_delete=models.SET_NULL)
    logpath = models.TextField(null=True, blank=True, verbose_name='回放日志存储路径')

    class Meta:
        verbose_name = '回放日志'
        verbose_name_plural = '回放日志'

