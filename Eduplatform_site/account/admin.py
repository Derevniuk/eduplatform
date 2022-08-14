from django.contrib import admin
from .models import (User,Teacher,Student,UserPhotos)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff')
    list_display_links = ('id', 'email')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'teacher', 'student')
    list_display_links = ('id','photo', 'teacher', 'student')


admin.site.register(User,UserAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(UserPhotos,PhotoAdmin)
