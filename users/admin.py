from django.contrib import admin
from users import models


# Register your models here.


class PermissionConfig(admin.ModelAdmin):
    list_display = ['permname', "url", "menu", "created_time", "updated_time", "create_user", "mod_user"]


class RoleConfig(admin.ModelAdmin):
    list_display = ["rolename", "created_time", "updated_time", "create_user", "mod_user"]


class MenuConfig(admin.ModelAdmin):
    list_display = ["menuname", "levelmenu", "icon", "created_time", "updated_time", "create_user", "mod_user"]


class UserProfileConfig(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "mphone", "email", "create_time", "last_login"]


class WorkOrderTypeConfig(admin.ModelAdmin):
    list_display = ["wk_name", "remark"]


admin.site.register(models.UserProfile, UserProfileConfig)
admin.site.register(models.Role, RoleConfig)
admin.site.register(models.Permission, PermissionConfig)
admin.site.register(models.Menu, MenuConfig)
admin.site.register(models.UserGroup)

