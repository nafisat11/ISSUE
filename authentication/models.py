# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(
        'first name', max_length=30, null=False, blank=False)
    last_name = models.CharField(
        'last name', max_length=150, null=False, blank=False)

    USERNAME_FIELD = 'email'  # Want user log in with email
    # Require user to enter first and last name when registering
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
