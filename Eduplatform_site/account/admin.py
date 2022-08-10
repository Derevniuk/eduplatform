from django.contrib import admin
from .models import User,Teacher,Student,UserPhotos

class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email',
                    'is_staff',
                    )
    list_display_links = ('id',
                          'email',
                          )



admin.site.register(User,UserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(UserPhotos)
