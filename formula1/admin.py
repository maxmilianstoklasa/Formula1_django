from django.contrib import admin
from django.db.models import Count

from .models import *
# Register your models here.
# Registrace modelů v administraci aplikace


@admin.register(Constructor)
class ConstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "driver_count")

    def get_queryset(self, request):
         queryset = super().get_queryset(request)
         queryset = queryset.annotate(
             _driver_count=Count("driver", distinct=True),
         )
         return queryset

    def driver_count(self, obj):
         return obj._driver_count

    driver_count.admin_order_field = "_driver_count"
    driver_count.short_description = "Number of drivers"


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "birth", "nationality")

    def birth_year(self, obj):
        return obj.birth_date

    birth_year.short_description = "Driver's birth"


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("title", "filesize", "driver_name")

    def driver_name(self, obj):
        return obj.driver.name

"""admin.site.register(Circuit)"""
