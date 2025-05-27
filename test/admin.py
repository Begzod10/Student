from django.contrib import admin
from .models import (
    TestBlock,
    TestQuestion,
    Subject,
    Test,
    StudentTest,
    StudentTestResult,
    StudentTestResultAnswer
)


@admin.register(TestBlock)
class TestBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'text', 'image')
    search_fields = ('text',)
    list_filter = ('test',)


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'block', 'test', 'answer', 'isTrue')
    search_fields = ('answer',)
    list_filter = ('block', 'test', 'isTrue')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'duration', 'is_mandatory')
    list_filter = ('field', 'subject', 'is_mandatory')
    search_fields = ('subject__name',)


@admin.register(StudentTest)
class StudentTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'test1', 'test2', 'name', 'surname', 'date', 'field')
    list_filter = ('date', 'field')
    search_fields = ('name', 'surname')


@admin.register(StudentTestResult)
class StudentTestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'result')
    search_fields = ('test__name',)


@admin.register(StudentTestResultAnswer)
class StudentTestResultAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'question', 'answer', 'is_true')
    list_filter = ('is_true',)
