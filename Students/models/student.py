from django.db import models
# from Organization.models import OrganizationType


class Shift(models.Model):
    name = models.CharField(max_length=250, null=True)
    organization_type = models.ForeignKey('Organization.OrganizationType', on_delete=models.SET_NULL, null=True)


class Student(models.Model):
    user = models.ForeignKey('Users.Users', on_delete=models.SET_NULL, null=True, blank=True)
    certificate = models.FileField(upload_to='certificate/', null=True, blank=True)
    region = models.ForeignKey('Students.region', on_delete=models.SET_NULL,null=True, blank=True)
    education_name = models.CharField(max_length=250, null=True)
    education_type = models.CharField(max_length=250, null=True)
    education_address = models.CharField(max_length=250, null=True)
    education_region = models.CharField(max_length=250, null=True)


class StudentRequest(models.Model):
    date = models.DateField()
    student_id = models.ForeignKey('Students.student', on_delete=models.SET_NULL, null=True, blank=True)
    organization_id = models.BigIntegerField()
    shift_id = models.BigIntegerField()
    field_id = models.BigIntegerField()
    # language_id = models.ForeignKey('Students.language', on_delete=models.SET_NULL, null=True, blank=True) #language qushilsa ulavorish kerak
    request_status = models.BigIntegerField()
    year_id = models.BigIntegerField()
    accepted = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    back_recovery = models.BooleanField(default=False)
    called_to_exam = models.BooleanField(default=False)
    present_in_exam = models.BooleanField(default=False)
    evaluated = models.BooleanField(default=False)
    contract_given = models.BooleanField(default=False)
    payed_status = models.BooleanField(default=False)
    accepted_to_study = models.BooleanField(default=False)
    degree_id = models.BigIntegerField()

    def __str__(self):
        return f"StudentRequest {self.id}"
