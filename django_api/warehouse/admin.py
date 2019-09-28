from django.contrib import admin

from . import models


@admin.register(models.Box)
class BoxAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ("__str__", "size", "available_size")
    readonly_fields = ("available_size",)


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass
