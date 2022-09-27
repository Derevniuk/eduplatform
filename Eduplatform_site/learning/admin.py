from django.contrib import admin

from .models import (Answer,
                     Article,
                     Attempt,
                     Course,
                     Question,
                     Test,
                     Topic,
                     Teacher,
                     Student,
                     Group,
                     Photo,
                     )

__all__ ={'CourseAdmin',
          'TopicAdmin',
          'ArticleAdmin',
          'TestAdmin',
          'QuestionAdmin',
          'AnswerAdmin',
          'AttemptAdmin',
          'TeacherAdmin',
          'StudentAdmin',
          'GroupAdmin',
          }


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
    list_display = ("id", "text",'is_important')
    list_display_link = ("id", "text",'is_important')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    list_display_link = ("id", "text")


class AttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "test", "student")
    list_display_link = ("id", "test", "student")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name")
    list_display_link = ("id", "group_name")


admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Photo)