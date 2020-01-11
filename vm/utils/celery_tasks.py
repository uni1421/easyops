from __future__ import absolute_import, unicode_literals

from celery import shared_task
from easyops.celery import app
import logging
import traceback
from vm import models
from vm.utils import pyvmutils
from pyVmomi import vim, vmodl
from pyVim.connect import SmartConnect, Disconnect


logger = logging.getLogger("vm")


@app.task
def SyncVcenterAllVM(host, user, password, port):
    try:
        logger.debug("host: {}, type: {}".format(host, type(host)))
        logger.debug("user: {}, type: {}".format(user, type(user)))
        logger.debug("password: {}, type: {}".format(password, type(password)))
        logger.debug("port: {}, type: {}".format(port, type(port)))
        service_instance = pyvm_utils.connect_vc(host=host, user=user, pwd=password, port=int(port))
        # service_instance = pyvm_utils.connect_vc()
        content = service_instance.RetrieveContent()
        hosts = pyvm_utils.get_all_hosts_info(content)
        print("hosts", hosts)
        for hostip, attribute in hosts.items():
            EsxiHostObj = models.EsxiHosts.objects.filter(ipaddress=hostip).first()
            if EsxiHostObj:
                EsxiHostObj.vendor = attribute.get("vendor")
                EsxiHostObj.model = attribute.get("model")
                EsxiHostObj.uuid = attribute.get("uuid")
                EsxiHostObj.fullname = attribute.get("fullName")
                EsxiHostObj.numcpupkgs = attribute.get("numCpuPkgs")
                EsxiHostObj.numcpucores = attribute.get("numCpuCores")
                EsxiHostObj.numcputhreads = attribute.get("numCpuThreads")
                EsxiHostObj.cpumhz = attribute.get("cpuMhz")
                EsxiHostObj.cpumodel = attribute.get("cpuModel")
                EsxiHostObj.datastorenum = attribute.get("datastore_num")
                EsxiHostObj.vmnum = attribute.get("vm_num")
                EsxiHostObj.uptime = attribute.get("uptime")
                EsxiHostObj.name = hostip
                EsxiHostObj.memorytotal = attribute.get("memorytotal")
                EsxiHostObj.memorysize = attribute.get("memorysize")
                EsxiHostObj.overallmemory = attribute.get("overallmemory")
                EsxiHostObj.powerstate = attribute.get("powerstate")
                EsxiHostObj.boottime = attribute.get("boottime")
                EsxiHostObj.save()
            else:
                models.EsxiHosts.objects.create(vendor=attribute.get("vendor"), model=attribute.get("model"),
                                                uuid=attribute.get("uuid"), fullname=attribute.get("fullName"),
                                                numcpupkgs=attribute.get("numCpuPkgs"),
                                                numcpucores=attribute.get("numCpuCores"),
                                                numcputhreads=attribute.get("numCpuThreads"),
                                                cpumhz=attribute.get("cpuMhz"),
                                                cpumodel=attribute.get("cpuModel"),
                                                datastorenum=attribute.get("datastore_num"),
                                                vmnum=attribute.get("vm_num"),
                                                memorysize=attribute.get("memorySize"),
                                                uptime=attribute.get("uptime"),
                                                name=hostip,
                                                memorytotal=attribute.get("memorytotal"),
                                                overallmemory=attribute.get("overallmemory"),
                                                powerstate=attribute.get("powerstate"),
                                                boottime=attribute.get("boottime"),
                                                )
        return
    except Exception as er:
        logger.error(er)
        logger.error(traceback.format_exc())





