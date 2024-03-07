from django.contrib import admin
from.models import *


# Register your models here.
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    search_fields=("title","price",)
    list_filter=("price",)
    list_display=("title","price","img")
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    search_fields=("fname","lname","phonenumber","content")
admin.site.register(category)
@admin.register(picture)
class pictureAdmin(admin.ModelAdmin):
    list_display=("product","img")
admin.site.site_header="مدیریت"
admin.site.site_title="میس کال"
admin.site.register(client)
admin.site.register(faktor)