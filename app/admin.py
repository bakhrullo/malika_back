from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from .models import *


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'name', 'get_html_photo', 'color', 'date']
    list_filter = ['model', 'color']
    list_editable = ['model', 'name', 'color']
    search_fields = ['name']

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Rasimi'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'get_html_photo_pass', 'get_html_photo_selfie', 'model', 'phone', 'color',
                    'type', 'status']
    list_filter = ['model', 'name', 'phone', 'type']
    search_fields = ['name']

    def get_html_photo_pass(self, object):
        if object.passport:
            return mark_safe(f"<img src='{object.passport.url}' width=50>")

    def get_html_photo_selfie(self, object):
        if object.selfie:
            return mark_safe(f"<img src='{object.selfie.url}' width=50>")

    get_html_photo_pass.short_description = 'Passport'
    get_html_photo_selfie.short_description = 'Selfie'


admin.site.unregister(Group)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Order, OrderAdmin)


admin.site.site_title = 'Admin Panel'
admin.site.site_header = 'Admin Panel'
