# -*- encoding: utf-8 -*-

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of username.
    """

    # Passing in email, first and last name since those fields are required to create a user
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must set an email address")
        if not first_name:
            raise ValueError("Users must set a first name")
        if not last_name:
            raise ValueError("Users must set a last name")

        email = self.normalize_email(email)
        # create the user and pass the parameters they require
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    # Passing in email, first and last name since those fields are required to create a superuser
    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, first_name, last_name, password, **extra_fields)
