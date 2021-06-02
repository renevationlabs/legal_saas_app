from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils import timezone


class UserManager(BaseUserManager):
    """Manager class for Custom User model"""
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email, first_name, last_name, password=None ):
        user = self.create_user(email,first_name,last_name, password)

        user.is_staff = True
        user.is_superuser = True
        user.is_subscribed=True

        user.save(using=self._db)

        return user


# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom User class
    """
    first_name = models.CharField(max_length=40, verbose_name='First name')
    last_name = models.CharField(max_length=40, verbose_name='Last name')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email address')
    is_staff = models.BooleanField(default=False, verbose_name='Is this person a staff member')
    is_superuser = models.BooleanField(verbose_name='Is this user a super user', default=False)
    is_active = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

