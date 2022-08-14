
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .mixins import DateTimeMixinModel
from .managers import CustomUserManager

__all__ = {'User','Teacher','Student','UserPhotos'}

class User(AbstractUser,DateTimeMixinModel,models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("staff status"),default=False,)
    is_active = models.BooleanField(_("active"),default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return f'{self.id} - {self.email} '

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.user}'

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.user}'

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

class UserPhotos(models.Model):
    photo = models.ImageField(upload_to='image/%Y/%m/%d/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.id}, path - {self.photo}'

    class Meta:
        verbose_name = _("user_photo")
        verbose_name_plural = _("user_photos")





