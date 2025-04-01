from django.db import models
from test.models.models import Test


class TestBlock(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='blocks', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    to_json = models.JSONField(default=dict, blank=True, null=True)
    image = models.ImageField(upload_to='test_blocks/', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.questions.all().delete()
        super().delete(*args, **kwargs)
