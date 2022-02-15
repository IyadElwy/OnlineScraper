from django.contrib import admin
from . import models

admin.site.register(models.Settings)
admin.site.register(models.Website)
admin.site.register(models.Product)
