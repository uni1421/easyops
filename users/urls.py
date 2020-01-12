from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login/$', views.LoginView, name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^reretpwd/$', views.ResetPaswordView.as_view(), name="reretpwd"),
    url(r'^custompwd/$', views.CustompwdView.as_view(), name="custompwd"),

    # 用户管理
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/add/$', views.UserDetailView.as_view()),
    url(r'^users/edit/([0-9]+)/$', views.UserDetailView.as_view()),
    url(r'^users/del/([0-9]+)/$', views.UserDetailView.as_view()),

    # 角色管理
    url(r'^users/role/$', views.RoleListView.as_view()),
    url(r'^users/role/add/$', views.RoleDetailView.as_view()),
    url(r'^users/role/edit/([0-9]+)/$', views.RoleDetailView.as_view()),
    url(r'^users/role/del/([0-9]+)/$', views.RoleDetailView.as_view()),

    # 权限管理
    url(r'^users/permission/$', views.PermissionListView.as_view()),
    url(r'^users/permission/add/$', views.PermissionDetailView.as_view()),
    url(r'^users/permission/edit/([0-9]+)/$', views.PermissionDetailView.as_view()),
    url(r'^users/permission/del/([0-9]+)/$', views.PermissionDetailView.as_view()),

    # 菜单管理
    url(r'^users/menu/$', views.MenuListView.as_view()),
    url(r'^users/menu/add/$', views.MenuDetailView.as_view()),
    url(r'^users/menu/edit/([0-9]+)/$', views.MenuDetailView.as_view()),
    url(r'^users/menu/del/([0-9]+)/$', views.MenuDetailView.as_view()),

    # 用户组管理
    url(r'^users/group/$', views.UsersGroupListView.as_view()),
    url(r'^users/group/add/$', views.UsersGroupDetailView.as_view()),
    url(r'^users/group/edit/([0-9]+)/$', views.UsersGroupDetailView.as_view()),
    url(r'^users/group/del/([0-9]+)/$', views.UsersGroupDetailView.as_view()),

    url(r'^500/$', views.Service500View, name="500"),
    url(r'^403/$', views.Service403View, name="403"),
    url(r'^404/$', views.Service404View, name="404"),

]
