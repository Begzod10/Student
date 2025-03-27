from django.db import models
from test.models.models import Test


class TestBlock(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='blocks', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    to_json = models.JSONField(default=dict, blank=True, null=True)
