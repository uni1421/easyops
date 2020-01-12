from django.contrib import admin
from ipmget import models
# Register your models here.


admin.site.register(models.DNSPools)
admin.site.register(models.IPDHCPools)
admin.site.register(models.IPAddr)

