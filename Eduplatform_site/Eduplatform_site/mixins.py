from django.db import models


class DateTimeMixinModel:
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
