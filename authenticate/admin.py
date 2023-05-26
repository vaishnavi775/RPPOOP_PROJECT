from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import validate
# Register your models here.

class validateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(validate, validateAdmin)


# class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     ...
# admin.site.register(User, UserAdmin)