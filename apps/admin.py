# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Model
from django.utils import timezone


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['date_joined']

    def is_new(self, obj):
        return (timezone.now() - obj.date_joined).days < 3

    is_new.boolean = True
    is_new.short_description = 'Yangi'

    def is_not_new(self, obj):
        return (timezone.now() - obj.date_joined).days > 3

    is_not_new.boolean = True
    is_not_new.short_description = 'Eski'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
