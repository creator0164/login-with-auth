from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email')


admin.site.register(Account, AccountAdmin)
