from django.contrib import admin
from .models import *


class UserCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_image')
    list_display_links = ('id', 'user_image')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'person')
    list_display_links = ('id', 'person')


admin.site.register(UserCode)
admin.site.register(Images)
admin.site.register(Person)
