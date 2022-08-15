from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.db import models
import account.mixins as mix
import account.models as m

__all__ = {'LearningCource', 'CourceTopic'}


class LearningCource(models.Model,mix.DateTimeMixinModel):
    cource_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(m.Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.cource_name}, teacher - {self.teacher}'

    class Meta:
        verbose_name = _("cource")
        verbose_name_plural = _("cources")


class CourceTopic(models.Model,mix.DateTimeMixinModel):
    topic_name = models.CharField(max_length=50)
    cource = models.ForeignKey(LearningCource, on_delete=models.CASCADE)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    difficulty = models.IntegerField(validators=[MinValueValidator(0,'Min difficulty value!')])

    def __str__(self):
        return f'{self.id}, {self.topic_name}, cource - {self.cource}'

    class Meta:
        verbose_name = _("cource_topic")
        verbose_name_plural = _("cource_topics")