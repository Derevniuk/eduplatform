from django.contrib import admin

from .models import Answer, Article, Attempt, Course, Question, Test, Topic


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_name")
    list_display_link = ("id", "course_name")


class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "topic_name", "numbering")
    list_display_link = ("id", "topic_name", "numbering")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "topic")
    list_display_link = ("id", "title", "topic")


class TestAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "topic")
    list_display_link = ("id", "title", "topic")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    list_display_link = ("id", "text")


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    list_display_link = ("id", "text")


class AttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "test", "student")
    list_display_link = ("id", "test", "student")


admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Attempt, AttemptAdmin)
