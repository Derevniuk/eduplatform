from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email',
                    'is_staff',
                    )
    list_display_links = ('id',
                          'email',
                          )


admin.site.register(User,UserAdmin)