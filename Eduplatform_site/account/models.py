from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from Eduplatform_site.mixins import DateTimeMixinModel

from .managers import CustomUserManager

__all__ = {"User", "Teacher", "Student", "Photo", "Group"}


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


class Teacher(models.Model, DateTimeMixinModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ManyToManyField("Photo")

    def __str__(self):
        return f"{self.id}, user-{self.user}"

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Student(models.Model, DateTimeMixinModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(null=True)
    photo = models.ManyToManyField("Photo")

    def __str__(self):
        return f"{self.id}, user - {self.user}"

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")


class Photo(models.Model, DateTimeMixinModel):
    photo = models.ImageField(
        upload_to="image/%Y/%m/%d/",
    )

    def __str__(self):
        return f"{self.id}, path-{self.photo}"

    class Meta:
        verbose_name = _("photo")
        verbose_name_plural = _("photos")
        unique_together = [
            "photo",
        ]


class Group(models.Model, DateTimeMixinModel):
    group_name = models.CharField(max_length=50)
    course = models.ForeignKey("learning.Course", on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.group_name}, teacher-{self.teacher}"

    class Meta:
        verbose_name = _("students_group")
        verbose_name_plural = _("students_groups")
