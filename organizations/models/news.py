from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, null=True)
    desc_json = models.JSONField(null=True, blank=True)
    img = models.FileField(upload_to='news/', null=True, blank=True)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, auto_now_add=True)
    deleted = models.BooleanField(default=False)


class NewsView(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    visitor_id = models.CharField(max_length=250, null=True)

    class Meta:
        unique_together = ('news', 'visitor_id')
