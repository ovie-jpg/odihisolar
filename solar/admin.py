from django.contrib import admin
from .models import Permission, Permissions

# Register your models here.

admin.site.register(Permission)
admin.site.register(Permissions)