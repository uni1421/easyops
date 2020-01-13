from django.conf.urls import url
from ipmget import views

urlpatterns = [
    url(r'^$', views.IpmtScanIPooolView.as_view()),
    url(r'^add/$', views.IpmtScanIPooolView.as_view()),
    url(r'^edit/([0-9]+)/$', views.IpmtScanIPooolView.as_view()),
    url(r'^del/([0-9]+)/$', views.IpmtScanIPooolView.as_view()),

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