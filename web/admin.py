from django.contrib import admin
from .models import Salesorderheader

# Register your models here.

class OrdensAdmin(admin.ModelAdmin):
    readonly_fields = ('salesorderid', 'orderdate', 'shipdate', 'status')
    list_display = ('salesorderid', 'orderdate', 'shipdate', 'status')
    search_fields = ('salesorderid', 'status')
    ordering = ('salesorderid',)
    list_filter = ('orderdate', 'shipdate')


admin.site.register(Salesorderheader, OrdensAdmin)