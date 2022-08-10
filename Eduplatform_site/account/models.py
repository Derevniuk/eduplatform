
import datetime
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
    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return f'{self.id} - {self.email} '

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Teacher(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.user_id}'

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.user_id}'

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("student")

class UserPhotos(models.Model):
    photo = models.ImageField(upload_to='image/%Y/%m/%d/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.id}, {self.photo}, {self.user}'

    class Meta:
        verbose_name = _("user_photo")
        verbose_name_plural = _("user_photo")





