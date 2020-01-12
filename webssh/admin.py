from django.contrib import admin
from vm import models
# Register your models here.

admin.site.register(models.VCenter)
admin.site.register(models.VMHosts)
admin.site.register(models.EsxiHosts)
