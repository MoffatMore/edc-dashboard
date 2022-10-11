from django.db import models


class TestModel(models.Model):

    f1 = models.CharField(
        max_length=25,
        null=True)

    class Meta:
        ordering = ('f1', )
