from django.contrib import admin

from sign.models import Event, Guest


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', id]
    # 搜索栏
    search_fields = ['name']
    # 过滤器
    list_filter = ['status']


class GuestAndmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    # 搜索栏
    search_fields = ['realname', 'phone']
    # 过滤器
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAndmin)
