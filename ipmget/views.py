from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import logging
import traceback
from vm import models
from vm.utils import celery_tasks
from ipmget.utils import vmutils
# Create your views here.

logger = logging.getLogger(__name__)


class VcenterDetailView(View):
    @method_decorator(login_required)
    def get(self, request):
        VCenterQuerySet = models.VCenter.objects.all()
        return render(request, "vmware/vcenter.html", {"VCenterQuerySet": VCenterQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        pass


class SyncVcenterDetailView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pass

    @method_decorator(login_required)
    def post(self, request):
        vcenterid = request.POST.get("vcenterid")
        VcenterObj = models.VCenter.objects.filter(id=vcenterid).first()
        if VcenterObj:
            celery_tasks.SyncVcenterAllVM.delay(VcenterObj.vc_ip, VcenterObj.vc_user, VcenterObj.vc_pwd, VcenterObj.vc_port)
            return JsonResponse({"code": 200, "message": "执行中"})
        else:
            return JsonResponse({"code": 500, "message": "系统出现异常,请记录下错误场景并及时与开发人员联系"})


class VMachineListView(View):
    @method_decorator(login_required)
    def get(self, request):
        VMHostQuerySet = models.VMHosts.objects.all()
        return render(request, "vmware/vmachine.html", {"VMHostQuerySet": VMHostQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        pass


class ClonseVMListView(View):
    @method_decorator(login_required)
    def get(self, request):
        IPAddrQuerySet, DNSPoolsQuerySet = vmutils.IPAvailableResources()

        return render(request, "vmware/createvmachine.html", {"IPAddrQuerySet": IPAddrQuerySet, "DNSPoolsQuerySet": DNSPoolsQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        pass





