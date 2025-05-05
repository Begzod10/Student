from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, null=True)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, auto_now_add=True)
    deleted = models.BooleanField(default=False)
    img = models.FileField(upload_to='news/', null=True, blank=True)


class NewsView(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    visitor_id = models.CharField(max_length=250, null=True)

    class Meta:
        unique_together = ('news', 'visitor_id')


class NewsBlock(models.Model):
    desc_json = models.JSONField(null=True, blank=True)
    img = models.FileField(upload_to='news/', null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='news_blocks')
    index = models.IntegerField(null=True)
    type_block = models.CharField(max_length=250, null=True)
