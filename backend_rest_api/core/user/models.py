from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **kwargs):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    placements = models.PositiveIntegerField(default=0)
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
