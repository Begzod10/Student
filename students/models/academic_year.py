from django.db import models


class AcademicYear(models.Model):
    from_date = models.DateField()
    to = models.DateField()


    def __str__(self):
        return f"{self.from_date} - {self.to}"

    class Meta:
        app_label = 'students'
