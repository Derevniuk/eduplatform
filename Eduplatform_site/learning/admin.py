from django.contrib import admin
from .models import CourceTopic,LearningCource

class LearningCourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'cource_name', 'teacher')
    list_display_link = ('id', 'cource_name', 'teacher')


class CourceTopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_name', 'difficulty')
    list_display_link = ('id', 'topic_name', 'difficulty')


admin.site.register(LearningCource,LearningCourceAdmin)
admin.site.register(CourceTopic,CourceTopicAdmin)