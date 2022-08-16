
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .mixins import DateTimeMixinModel
from .managers import CustomUserManager
import learning.models as learning_models


__all__ = {'User','Teacher','Student','Photo','Group'}


class User(AbstractBaseUser,PermissionsMixin,DateTimeMixinModel,models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("staff status"),default=False,)
    is_active = models.BooleanField(_("active"),default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return f'{self.id}, {self.email} '

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Teacher(models.Model,DateTimeMixinModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.user}'

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Student(models.Model,DateTimeMixinModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(learning_models.Course, on_delete= models.CASCADE,null=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE,null=True)
    completed_tests = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.id}, user - {self.user}, course - {self.course}, group - {self.group}'

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

class Photo(models.Model,DateTimeMixinModel):
    photo = models.ImageField(upload_to='image/%Y/%m/%d/')
    teacher = models.ForeignKey(Teacher,models.CASCADE,blank=True,null=True)
    student = models.ForeignKey(Student, models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.id}, path - {self.photo}'

    class Meta:
        verbose_name = _("photo")
        verbose_name_plural = _("photos")


class Group(models.Model,DateTimeMixinModel):
    group_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.group_name}, teacher - {self.teacher}'

    class Meta:
        verbose_name = _("students_group")
        verbose_name_plural = _("students_groups")


