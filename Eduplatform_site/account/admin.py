from django.contrib import admin

from .models import Group, Photo, Student, Teacher, User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_staff")
    list_display_links = ("id", "email")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name")
    list_display_link = ("id", "group_name")


admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Photo)
