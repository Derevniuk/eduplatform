

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .mixins import DateTimeMixinModel
from .managers import CustomUserManager


class User(DateTimeMixinModel,AbstractUser):
    username = models.CharField(_("username"),max_length=150)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("staff status"),default=False,)
    is_active = models.BooleanField(_("active"),default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id} - {self.email} '

    class Meta:
        verbose_name = _("Custom_user")
        verbose_name_plural = _("Castom_users")



