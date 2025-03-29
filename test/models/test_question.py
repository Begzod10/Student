from django.db import models
from test.models.test_block import TestBlock
from test.models.models import Test


class TestQuestion(models.Model):
    block = models.ForeignKey(TestBlock, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    isTrue = models.BooleanField(default=False)
    answer = models.CharField(max_length=255, null=True, blank=True)
    to_json = models.JSONField(default=dict, blank=True, null=True)
