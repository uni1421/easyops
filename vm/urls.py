from django.conf.urls import url
from vm import views

urlpatterns = [
    url(r'^vcentermg/$', views.VcenterDetailView.as_view()),
    url(r'^vcentermg/add/$', views.VcenterDetailView.as_view()),
    url(r'^vcentermg/edit/([0-9]+)/$', views.VcenterDetailView.as_view()),
    url(r'^vcentermg/del/([0-9]+)/$', views.VcenterDetailView.as_view()),
    url(r'^vcentermg/vcsyncdata/$', views.SyncVcenterDetailView.as_view()),
    url(r'^vmmachine/$', views.VMachineListView.as_view()),
    url(r'^vmmachine/add/$', views.VcenterDetailView.as_view()),
    url(r'^vmmachine/edit/([0-9]+)/$', views.VcenterDetailView.as_view()),
    url(r'^vmmachine/del/([0-9]+)/$', views.VcenterDetailView.as_view()),
    url(r'^vmmachine/clonevm/', views.ClonseVMListView.as_view()),
]