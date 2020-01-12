from django.conf.urls import url
from users import views

urlpatterns = [
    # 用户管理
    url(r'^/$', views.UserListView.as_view()),
    url(r'^add/$', views.UserDetailView.as_view()),
    url(r'^edit/([0-9]+)/$', views.UserDetailView.as_view()),
    url(r'^del/([0-9]+)/$', views.UserDetailView.as_view()),

    # 角色管理
    url(r'^/role/$', views.RoleListView.as_view()),
    url(r'^/role/add/$', views.RoleDetailView.as_view()),
    url(r'^/role/edit/([0-9]+)/$', views.RoleDetailView.as_view()),
    url(r'^/role/del/([0-9]+)/$', views.RoleDetailView.as_view()),

    # 权限管理
    url(r'^/permission/$', views.PermissionListView.as_view()),
    url(r'^/permission/add/$', views.PermissionDetailView.as_view()),
    url(r'^/permission/edit/([0-9]+)/$', views.PermissionDetailView.as_view()),
    url(r'^/permission/del/([0-9]+)/$', views.PermissionDetailView.as_view()),

    # 菜单管理
    url(r'^/menu/$', views.MenuListView.as_view()),
    url(r'^/menu/add/$', views.MenuDetailView.as_view()),
    url(r'^/menu/edit/([0-9]+)/$', views.MenuDetailView.as_view()),
    url(r'^/menu/del/([0-9]+)/$', views.MenuDetailView.as_view()),

    # 用户组管理
    url(r'^/group/$', views.UsersGroupListView.as_view()),
    url(r'^/group/add/$', views.UsersGroupDetailView.as_view()),
    url(r'^/group/edit/([0-9]+)/$', views.UsersGroupDetailView.as_view()),
    url(r'^/group/del/([0-9]+)/$', views.UsersGroupDetailView.as_view()),

    url(r'^500/$', views.Service500View, name="500"),
    url(r'^403/$', views.Service403View, name="403"),
    url(r'^404/$', views.Service404View, name="404"),

]
