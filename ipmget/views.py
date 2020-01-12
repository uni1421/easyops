from django.shortcuts import render, redirect
from ipmget import models
from django.views import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import logging
from ipmget.utils import celery_tasks
# Create your views here.

logger = logging.getLogger("ipmanagement")


class IpmtScanIPooolView(View):

    @method_decorator(login_required)
    def get(self, request):

        IPollsQuerySet = models.IPools.objects.all()

        return render(request, "ipmanagement/ipmt.html", {"IPollsQuerySet": IPollsQuerySet})

    @method_decorator(login_required)
    def post(self, request):
        logger.info("======================开始执行扫描=======================")
        id = request.POST.get("id")
        if id:
            if id.isdigit():
                IPollsObj = models.IPools.objects.filter(id=id).first()
                if IPollsObj:
                    tasks.ScanHosts.delay(IPollsObj.ip_start, IPollsObj.ip_end)
                    logger.info("======================结束执行扫描=======================")
                    return JsonResponse({"code": 200, "message": "执行中"})
        else:
            return JsonResponse({"code": 500, "message": "系统出现异常,请记录下错误场景并及时与开发人员联系"})


class IpmtIpSearchView(View):

    @method_decorator(login_required)
    def get(self, request):

        return render(request, "ipmanagement/ipsearch.html")


class IpmtDNSmtView(View):

    @method_decorator(login_required)
    def get(self, request):

        DNSPollsQuerySet = models.DNSPools.objects.all()
        print("DNSPollsQuerySet", DNSPollsQuerySet)
        return render(request, "ipmanagement/dnsmt.html", {"DNSPollsQuerySet": DNSPollsQuerySet})


class IPAddrsView(View):
    @method_decorator(login_required)
    def get(self, request):

        IPoolsQuerySet = models.IPAddr.objects.all()
        return render(request, "ipmanagement/ipaddrs.html", {"IPoolsQuerySet": IPoolsQuerySet})

