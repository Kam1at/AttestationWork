from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from holders.models import Holders


@admin.register(Holders)
class HoldersAdmin(admin.ModelAdmin):
    list_display = ("id", "instance", "name", "contacts", "link_to_supplier", "indebtedness", "created_time")
    list_filter = ("contacts__city",)
    actions = ("clear_arrears",)

    def link_to_supplier(self, obj):
        if obj.supplier:
            link = reverse("admin:chain_chain_change", args=[obj.supplier_id])
            return format_html('<a href="{}">Редактировать {}</a>', link, obj.supplier)
        return '-'

    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)

    link_to_supplier.short_description = "Поставщик"
    clear_arrears.short_description = "Очистить задолженность"

