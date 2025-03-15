from django.db import models


class EducationLanguage(models.Model):
    name = models.CharField(max_length=250, null=True)
    img = models.FileField(upload_to='education_language/', null=True, blank=True)

    class Meta:
        app_label = 'education'
