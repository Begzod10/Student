from django.db import models


class Jobs(models.Model):
    name = models.CharField(max_length=250, null=True)
