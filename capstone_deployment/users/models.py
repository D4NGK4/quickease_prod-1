from django.db import models
from utils.model import Model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin, Model):
    firstname = models.CharField(_("First Name"), max_length=100)
    lastname = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]
    
    objects = CustomUserManager()
    
    class Meta: 
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    


    
