from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils import timezone


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
    date_joined = models.DateTimeField(verbose_name='Date joined',default=timezone.now() )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

