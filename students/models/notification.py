from django.db import models


class Notification(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE)
    desc_json = models.JSONField(null=True, blank=True)
    student = models.ForeignKey('students.student', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        app_label = 'students'
