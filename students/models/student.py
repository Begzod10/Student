from django.db import models


# from organization.models.models import OrganizationType


class Shift(models.Model):
    name = models.CharField(max_length=250, null=True)
    organization_type = models.ForeignKey('organization.OrganizationType', on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'students'


class Student(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.SET_NULL, null=True, blank=True)
    certificate = models.FileField(upload_to='certificate/', null=True, blank=True)
    region = models.ForeignKey('students.region', on_delete=models.SET_NULL, null=True, blank=True)
    education_name = models.CharField(max_length=250, null=True)
    education_type = models.CharField(max_length=250, null=True)
    education_address = models.CharField(max_length=250, null=True)
    education_region = models.CharField(max_length=250, null=True)

    class Meta:
        app_label = 'students'


class StudentRequest(models.Model):
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey('students.student', on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey('organization.Organization', on_delete=models.SET_NULL, null=True)
    shift = models.ForeignKey('students.Shift', on_delete=models.SET_NULL, null=True, blank=True)
    field = models.ForeignKey('organization.OrganizationFields', on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey('education.EducationLanguage', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    request_status = models.BigIntegerField()
    year = models.ForeignKey('students.AcademicYear', on_delete=models.SET_NULL, null=True, blank=True)
    accepted = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    back_recovery = models.BooleanField(default=False)
    called_to_exam = models.BooleanField(default=False)
    present_in_exam = models.BooleanField(default=False)
    evaluated = models.BooleanField(default=False)
    contract_given = models.BooleanField(default=False)
    payed_status = models.BooleanField(default=False)
    accepted_to_study = models.BooleanField(default=False)
    degree = models.ForeignKey('organization.OrganizationDegrees', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"StudentRequest {self.id}"

    class Meta:
        app_label = 'students'