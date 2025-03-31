from django.db import models


class AcademicYear(models.Model):
    from_date = models.DateField()
    to = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_date} - {self.to}"

    class Meta:
        app_label = 'students'
