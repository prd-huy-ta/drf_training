from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        abstract = True
