from django.contrib import admin
from .models import Topic,Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name')
    list_display_link = ('id', 'course_name')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_name', 'numbering')
    list_display_link = ('id', 'topic_name', 'numbering')


admin.site.register(Course,CourseAdmin)
admin.site.register(Topic,TopicAdmin)