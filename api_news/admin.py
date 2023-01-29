from django.contrib import admin
from .models import Type, News


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    list_display_links = ('name',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'type')
    list_display_links = ('name',)


admin.site.register(Type, TypeAdmin)
admin.site.register(News, NewsAdmin)
