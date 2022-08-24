from account.models import Student, Teacher
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from Eduplatform_site.mixins import DateTimeMixinModel

__all__ = {"Course", "Topic", "Article", "Test", "Question", "Answer", "Attempt"}


class Course(models.Model, DateTimeMixinModel):
    course_name = models.CharField(max_length=50)
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return f"{self.course_name}"


class Topic(models.Model, DateTimeMixinModel):
    topic_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    numbering = models.IntegerField(validators=[MinValueValidator(0, "Min number value!")])

    class Meta:
        verbose_name = _("course_topic")
        verbose_name_plural = _("course_topics")
        ordering = [
            "numbering",
        ]

    def __str__(self):
        return f"{self.id}, {self.topic_name}, course - {self.course}"


class Article(models.Model, DateTimeMixinModel):
    creator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("topic_articles")
        verbose_name_plural = _("topic_articles")


class Test(models.Model, DateTimeMixinModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("topic_test")
        verbose_name_plural = _("topic_tests")


class Question(models.Model, DateTimeMixinModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = _("test_question")
        verbose_name_plural = _("test_questions")


class Answer(models.Model, DateTimeMixinModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=50, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = _("question_answer")
        verbose_name_plural = _("question_answers")


class Attempt(models.Model, DateTimeMixinModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.test} - {self.student}"

    class Meta:
        verbose_name = _("test_attempt")
        verbose_name_plural = _("test_attempts")
