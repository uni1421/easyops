from ipmget import models
from django.db.models import Q


def IPAvailableResources():
    """
    提供VM查询可用IP资源及DNS
    :return:
    """
    IPAddrQuerySet = models.IPAddr.objects.filter(Q(ip_status="未分配") and Q(ip_ping="down")).distinct()
    DNSPoolsQuerySet = models.DNSPools.objects.all()
    return IPAddrQuerySet, DNSPoolsQuerySet


