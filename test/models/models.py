from django.db import models

from organizations.models.organization_fields import OrganizationFields
from test.models.subject import Subject


class Test(models.Model):
    name = models.CharField(null=True, blank=True)
    field = models.ForeignKey(OrganizationFields, on_delete=models.CASCADE, related_name='blocks', null=True,
                              blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.BigIntegerField(null=True, blank=True)
    is_mandatory = models.BooleanField(null=True, blank=True)


class StudentTest(models.Model):
    student = models.ForeignKey('students.student', on_delete=models.SET_NULL, null=True, blank=True)
    test1 = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, blank=True, related_name='test1')
    test2 = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, blank=True, related_name='test2')
    name = models.CharField(null=True, blank=True)
    field = models.ForeignKey(OrganizationFields, on_delete=models.SET_NULL, null=True, blank=True)
    surname = models.CharField(null=True, blank=True)


class StudentTestResult(models.Model):
    test = models.ForeignKey(StudentTest, on_delete=models.SET_NULL, null=True, blank=True)
    result = models.BigIntegerField(null=True, blank=True)
    true_answers = models.JSONField(null=True, blank=True)


class StudentTestResultAnswer(models.Model):
    result = models.ForeignKey(StudentTestResult, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey('test.TestBlock', on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.ForeignKey('test.TestQuestion', on_delete=models.SET_NULL, null=True, blank=True)
    is_true = models.BooleanField(null=True, blank=True)
