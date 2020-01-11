from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Role(models.Model):
    """
    角色表
    """
    rolename = models.CharField(max_length=32, verbose_name="角色名称", help_text="角色名称")
    permissions = models.ManyToManyField(to="Permission", verbose_name="关联权限", help_text="关联权限")
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间", help_text="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间", help_text="最后更新时间")
    create_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="角色创建者", help_text="角色创建者")
    mod_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="最后修改者", help_text="最后修改者")

    def __str__(self):
        return self.rolename

    class Meta:
        db_table = "role"
        verbose_name_plural = "角色表"
        verbose_name = "角色表"


class Permission(models.Model):

    permname = models.CharField(max_length=128, verbose_name="权限名称", help_text="权限名称")
    url = models.CharField(max_length=128, null=True, blank=True, verbose_name="URL", help_text="URL, 是一级菜单时为空")
    menu = models.ForeignKey(to="Menu", null=True, blank=True, on_delete=models.CASCADE, verbose_name="菜单",
                             help_text="关联菜单表，通过menu是否有值，有值是菜单，无值是权限URL")
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间", help_text="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    create_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="权限创建者",
                                   help_text="权限创建者")
    mod_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="最后修改者", help_text="最后修改者")

    def __str__(self):
        return self.permname

    class Meta:
        db_table = "permission"
        verbose_name_plural = "权限表"
        verbose_name = "权限表"


class Menu(models.Model):
    """
    菜单表
    """
    menuname = models.CharField(max_length=32, verbose_name="菜单名称", help_text="菜单名称")
    levelmenu = models.ForeignKey(to="self", null=True, blank=True, verbose_name="父级菜单", help_text="如果是子菜单，请选择父菜单")
    icon = models.CharField(max_length=512, null=True, blank=True, verbose_name="class 样式", help_text="class样式")
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间", help_text="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    create_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="菜单创建者", help_text="菜单创建者")
    mod_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="最后修改者", help_text="最后修改者")

    def __str__(self):
        return self.menuname

    class Meta:
        db_table = "menu"
        verbose_name_plural = "菜单表"
        verbose_name = "菜单表"


class UserProfile(AbstractUser):
    """
    系统用户表
    """
    phone = models.CharField(max_length=32, verbose_name="电话", default=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    mod_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    email = models.CharField(max_length=254, unique=True, verbose_name="邮箱")
    mphone = models.CharField(max_length=254, default="", verbose_name="手机号码")
    create_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="创建者", help_text="创建者")
    mod_user = models.CharField(max_length=32, default="", null="", blank=True, verbose_name="最后修改者", help_text="最后修改者")
    roles = models.ManyToManyField(to="Role", verbose_name="角色", help_text="用户所属角色")
    hosts = models.ManyToManyField(to="webssh.HostRemote", blank=True, verbose_name="管理主机")
    hostgroup = models.ManyToManyField(to="webssh.HostGroup", blank=True, verbose_name="管理主机组")

    class Meta:
        verbose_name_plural = "用户表"
        verbose_name = "用户表"


class UserGroup(models.Model):
    """
    用户组/部门表/门店表
    """
    groupname = models.CharField(max_length=128, verbose_name="用户组", help_text="用户组")

    def __str__(self):
        return self.groupname

    class Meta:
        verbose_name_plural = "用户组"
        verbose_name = "用户组"

