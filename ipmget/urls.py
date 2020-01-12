from django.conf.urls import url
from ipmget import views

urlpatterns = [
    url(r'^ipmget/$', views.IpmtScanIPooolView.as_view()),
    url(r'^ipmget/add/$', views.IpmtScanIPooolView.as_view()),
    url(r'^ipmget/edit/([0-9]+)/$', views.IpmtScanIPooolView.as_view()),
    url(r'^ipmget/del/([0-9]+)/$', views.IpmtScanIPooolView.as_view()),

    url(r'^ipmgaddr/$', views.IPAddrsView.as_view()),

    url(r'^ipsearch/$', views.IpmtIpSearchView.as_view()),
    url(r'^ipsearch/add/$', views.IpmtIpSearchView.as_view()),
    url(r'^ipsearch/edit/([0-9]+)/$', views.IpmtIpSearchView.as_view()),
    url(r'^ipsearch/del/([0-9]+)/$', views.IpmtIpSearchView.as_view()),

    url(r'^ipdns/$', views.IpmtDNSmtView.as_view()),
    url(r'^ipdns/add/$', views.IpmtDNSmtView.as_view()),
    url(r'^ipdns/edit/([0-9]+)/$', views.IpmtDNSmtView.as_view()),
    url(r'^ipdns/del/([0-9]+)/$', views.IpmtDNSmtView.as_view()),
]