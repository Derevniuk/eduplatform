from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from Eduplatform_site.mixins import DateTimeMixinModel

from .managers import CustomUserManager

__all__ = {"User"}


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixinModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(_("active"), default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.email} "

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['-pk']



