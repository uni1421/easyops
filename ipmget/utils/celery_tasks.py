from __future__ import absolute_import, unicode_literals

from celery import shared_task
from ops.celery import app
import logging
import traceback
import nmap
import re
import os
from ipmanagement import models

logger = logging.getLogger("ipmanagement")

nm = nmap.PortScanner()


# @app.task
# def ScanHosts(startip='192.168.104.2', stopip='192.168.104.200', arguments='-sP'):
#     """
#     :param hosts: hosts='192.168.102.0/24', hosts='192.168.104.2-200',
#     :param arguments:
#     :return:
#     """
#     logger.info("==============定时任务ScanHosts开始==============")
#     logger.info("startip: {}".format(startip))
#     logger.info("stopip: {}".format(stopip))
#     logger.info("arguments: {}".format(arguments))
#     if re.match('^[0-9]{3}.[0-9]{3}.[0-9]{1,3}.[0-9]{1,3}', startip) or re.match('^[0-9]{3}.[0-9]{3}.[0-9]{1,3}.[0-9]{1,3}', stopip):
#
#         # ipaddr = startip.split(".")[0] + "." + startip.split(".")[1] + "." + startip.split(".")[2]
#         hosts = startip + "-" + stopip.split('.')[3]
#         total_ipdict = dict()
#         for i in range(int(startip.split('.')[3]), int(stopip.split('.')[3])):
#             total_ipdict[(startip.split(".")[0] + "." + startip.split(".")[1] + "." + startip.split(".")[2] + "." + str(i))] = "down"
#         try:
#             nm.scan(hosts=hosts, arguments=arguments)
#             hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
#             for host, status in hosts_list:
#                 # print('{}: {}'.format(host, status))
#                 if host in total_ipdict:
#                     total_ipdict[host] = status
#
#             logger.debug("{}".format(total_ipdict))
#             for ip, stats in total_ipdict.items():
#                 ipobj = models.IPAddr.objects.filter(ipaddr=ip).first()
#                 if ipobj:
#                     ipobj.ip_ping = stats
#                     ipobj.save()
#                 else:
#                     if stats == "up":
#                         models.IPAddr.objects.create(ipaddr=ip, ip_ping=stats, ip_status="使用中")
#                     elif stats == "down":
#                         models.IPAddr.objects.create(ipaddr=ip, ip_ping=stats, ip_status="未分配")
#
#             logger.info("==============定时任务ScanHosts结束==============")
#
#             return
#
#         except Exception as er:
#             logger.error("定时任务ScanHosts执行出现异常: {}".format(er))
#             logger.error(traceback.format_exc())
#             return total_ipdict
#
#     else:
#         logger.error("startip: {}".format(startip))
#         logger.error("stopip: {}".format(stopip))
#         logger.error("arguments: {}".format(arguments))
#         return

@app.task
def ScanHosts(startip='192.168.104.2', stopip='192.168.104.200', arguments='-sP'):
    """
    :param hosts: hosts='192.168.102.0/24', hosts='192.168.104.2-200',
    :param arguments:
    :return:
    """
    logger.info("==============定时任务ScanHosts开始==============")
    logger.info("startip: {}".format(startip))
    logger.info("stopip: {}".format(stopip))
    logger.info("arguments: {}".format(arguments))
    if re.match('^[0-9]{3}.[0-9]{3}.[0-9]{1,3}.[0-9]{1,3}', startip) or re.match('^[0-9]{3}.[0-9]{3}.[0-9]{1,3}.[0-9]{1,3}', stopip):

        # ipaddr = startip.split(".")[0] + "." + startip.split(".")[1] + "." + startip.split(".")[2]
        hosts = startip + "-" + stopip.split('.')[3]
        total_ipdict = dict()
        for i in range(int(startip.split('.')[3]), int(stopip.split('.')[3])):
            total_ipdict[(startip.split(".")[0] + "." + startip.split(".")[1] + "." + startip.split(".")[2] + "." + str(i))] = "down"
        try:
            nm.scan(hosts=hosts, arguments=arguments)
            hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
            for host, status in hosts_list:
                # print('{}: {}'.format(host, status))
                if host in total_ipdict:
                    total_ipdict[host] = status

            logger.debug("{}".format(total_ipdict))
            for ip, stats in total_ipdict.items():
                ipobj = models.IPAddr.objects.filter(ipaddr=ip).first()
                if ipobj:
                    ipobj.ip_ping = stats
                    ipobj.save()
                else:
                    if stats == "up":
                        models.IPAddr.objects.create(ipaddr=ip, ip_ping=stats, ip_status="使用中")
                    elif stats == "down":
                        models.IPAddr.objects.create(ipaddr=ip, ip_ping=stats, ip_status="未分配")

            logger.info("==============定时任务ScanHosts结束==============")
            return

        except Exception as er:
            logger.error("定时任务ScanHosts执行出现异常: {}".format(er))
            logger.error(traceback.format_exc())
            return total_ipdict

    else:
        logger.error("startip: {}".format(startip))
        logger.error("stopip: {}".format(stopip))
        logger.error("arguments: {}".format(arguments))
        return


if __name__ == '__main__':
    ScanHosts()

