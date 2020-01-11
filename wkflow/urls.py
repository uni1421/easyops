from django.conf.urls import url
from wkflow import views

urlpatterns = [
    # 新建工单
    url(r'^work/$', views.WorkModelSelectView.as_view()),
    url(r'^work/add/([0-9]+)/$', views.WorkAddView),
    url(r'^work/edit/([0-9]+)/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/del/([0-9]+)/$', views.UsersGroupDetailView.as_view()),

    # 待处理工单
    url(r'^wkhandle/$', views.WorkHandleListView.as_view()),
    url(r'^wkhandle/add/$', views.WorkHandleListView.as_view()),
    url(r'^wkhandle/edit/([0-9]+)/$', views.WorkHandleEditView.as_view()),
    url(r'^wkhandle/del/([0-9]+)/$', views.WorkHandleListView.as_view()),

    # 与我相关的工单
    url(r'^work/relevant/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/relevant/add/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/relevant/edit/([0-9]+)/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/relevant/del/([0-9]+)/$', views.UsersGroupDetailView.as_view()),

    # 工单流程管理
    url(r'^work/model/$', views.WorkModelListView.as_view()),
    url(r'^work/model/add/$', views.WorkModelListView.as_view()),
    url(r'^work/model/edit/([0-9]+)/$', views.WorkModelListView.as_view()),
    url(r'^work/model/del/([0-9]+)/$', views.WorkModelListView.as_view()),

    # 工单问题分类管理
    url(r'^work/classify/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/classify/add/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/classify/([0-9]+)/$', views.UsersGroupDetailView.as_view()),
    url(r'^work/classify/([0-9]+)/$', views.UsersGroupDetailView.as_view()),

    # 工单查询
    url(r'^wksearch/$', views.WorkSearchView.as_view()),
    url(r'^wksearchclassify/$', views.WorkSearchClassifyView.as_view()),

]
