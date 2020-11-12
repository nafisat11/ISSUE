# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import CustomUser


class CustomUserAdmin(UserAdmin):
    ordering = ('email',)

    list_display = (
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'last_login',
        'is_staff'
    )

    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, CustomUserAdmin)
