from django.contrib import admin

from mailings.models import Client, MailingSettings


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    list_filter = ('name', 'email',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('client', 'title', 'periodicity', 'status',)
    list_filter = ('client', 'title',)
