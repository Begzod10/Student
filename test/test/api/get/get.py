import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from test.models.subject import Subject
from test.models.models import Test, StudentTestResult, StudentTest
from test.models.test_block import TestBlock
from test.test.filtersets.testflter import TestFilter
from test.test.serializers.get.get import TestRetrieveSerializer, TestListSerializer, StudentTestResultSerializer
import pprint
from organizations.models.organization_fields import OrganizationFields


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestRetrieveSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TestRetrieveViewForHome(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestRetrieveSerializer

    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        surname = request.query_params.get('surname')
        student = request.query_params.get('student')
        field_id = request.query_params.get('field')
        field_id = int(field_id) if field_id else None
        get_field = OrganizationFields.objects.filter(id=field_id).first()
        main_test, second_test = None, None
        if field_id:
            tests = Test.objects.filter(is_mandatory=False, field__id=field_id, status=True).order_by('?')[:2]
            main_test = tests[0] if len(tests) > 0 else None
            second_test = tests[1] if len(tests) > 1 else None

        student_main_test_add = StudentTest.objects.filter(
            name=name,
            surname=surname,
            student=student if student else None,
            test1=main_test,
            test2=second_test,
            field_id=field_id
        ).first()

        if not student_main_test_add and main_test and second_test:
            student_main_test_add = StudentTest.objects.create(
                name=name,
                surname=surname,
                student=student if student else None,
                test1=main_test if main_test else None,
                test2=second_test if second_test else None,
                field_id=field_id
            )
        else:
            return Response({f"msg": f"Bu {get_field.name} bo'limi uchun testlar mavjud emas", "status": False})
        subject_names = ["Ona tili", "Matematika", "Tarix"]
        mandatory_subjects = []
        total_duration = 0

        if main_test:
            total_duration += main_test.duration or 0
        if second_test:
            total_duration += second_test.duration or 0

        for subject_name in subject_names:
            tests = Test.objects.filter(is_mandatory=True, subject__name__icontains=subject_name, status=True,
                                        field__id=field_id).order_by('?')
            get_test = Test.objects.filter(is_mandatory=True, subject__name__icontains=subject_name, status=True,
                                           field__id=field_id).first()
            exist_student_test = StudentTest.objects.filter(
                name=name,
                surname=surname,
                student=student if student else None,
                field_id=field_id,
                test1=get_test
            ).first()
            if not exist_student_test and get_test:
                exist_student_test = StudentTest.objects.create(
                    name=name,
                    surname=surname,
                    student=student if student else None,
                    test1=get_test,
                    field_id=field_id
                )
            if tests.exists():
                selected = random.choice(tests)
                duration = selected.duration or 0
                total_duration += duration
                print("exist_student_test", exist_student_test)
                mandatory_subjects.append({
                    "subject": subject_name,
                    "test_id": selected.id,
                    "student_test_id": exist_student_test.id if exist_student_test else None,
                    "duration": duration,
                    "question_count": TestBlock.objects.filter(test=selected).count()
                })
            else:
                mandatory_subjects.append({
                    "subject": subject_name,
                    "test_id": None,
                    "duration": 0,
                    "question_count": 0
                })

        response = {
            "main_test": {
                "id": main_test.id if main_test else None,
                "duration": main_test.duration if main_test else 0,
                "student_test_id": student_main_test_add.id if student_main_test_add else None,
                "question_count": TestBlock.objects.filter(test=main_test).count() if main_test else 0,
            },
            "second_test": {
                "id": second_test.id if second_test else None,
                "duration": second_test.duration if second_test else 0,
                "student_test_id": student_main_test_add.id if student_main_test_add else None,
                "question_count": TestBlock.objects.filter(test=second_test).count() if second_test else 0,
            },
            "mandatory_tests": mandatory_subjects,
            "total_mandatory_duration": total_duration
        }

        return Response(response)


class TestListApiView(generics.ListAPIView):
    queryset = Test.objects.order_by('-id').all()
    serializer_class = TestListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TestFilter


class TestListApiViewForHome(APIView):
    def get(self, request):
        tests = Test.objects.filter(is_mandatory=False, status=True)
        subjects = Subject.objects.filter(test__in=tests).distinct()

        data = []
        for subject in subjects:
            data.append({
                "name": subject.name,
                "id": subject.id
            })
        return Response(data)

    def post(self, request):
        main_id = request.data.get("main_id")
        second_id = request.data.get("second_id")

        main_test = Test.objects.filter(subject_id=main_id, is_mandatory=False).order_by('?').first()
        second_test = Test.objects.filter(subject_id=second_id, is_mandatory=False).order_by('?').first()

        subject_names = ["Ona tili", "Matematika", "Tarix"]
        mandatory_subjects = []
        total_duration = 0
        total_duration += main_test.duration if main_test else 0
        total_duration += second_test.duration if second_test else 0

        for subject_name in subject_names:
            tests = Test.objects.filter(is_mandatory=True, subject__name__icontains=subject_name, status=True)
            if tests.exists():
                selected = random.choice(tests)
                duration = selected.duration or 0
                total_duration += duration

                mandatory_subjects.append({
                    "subject": subject_name,
                    "test_id": selected.id,
                    # "test_name": selected.name,
                    "duration": duration,
                    "question_count": TestBlock.objects.filter(test=selected).count()
                })
            else:
                mandatory_subjects.append({
                    "subject": subject_name,
                    "test_id": None,
                    "test_name": None,
                    "duration": 0,
                    "question_count": 0
                })

        question_count = 0
        if main_test and hasattr(main_test, "question_set"):
            question_count = main_test.question_set.count()

        response = {
            "main_test": {
                "id": main_test.id if main_test else None,
                # "name": main_test.name if main_test else None,
                "question_count": TestBlock.objects.filter(test=main_test).count(),
                "duration": main_test.duration if main_test else 0,
            },
            "second_test": {
                "id": second_test.id if second_test else None,
                # "name": second_test.name if second_test else None,
                "duration": second_test.duration if second_test else 0,
                "question_count": TestBlock.objects.filter(test=second_test).count()

            },
            "mandatory_tests": mandatory_subjects,
            "total_mandatory_duration": total_duration
        }

        return Response(response)


class StudentTestResultListApiView(generics.ListAPIView):
    queryset = StudentTestResult.objects.all()
    serializer_class = StudentTestResultSerializer

    def get_queryset(self):
        student_id = self.request.query_params.get('student_id')
        organization_id = self.request.query_params.get('organization_id')

        if student_id:
            return self.queryset.filter(test__student_id=student_id)

        elif organization_id:
            return self.queryset.filter(
                test__field__organization_id=organization_id
            )

        return self.queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        test_id = instance.test.id
        get_test = StudentTest.objects.filter(id=test_id).first()
        student_results = StudentTestResult.objects.filter(test_id=test_id)
        student_results.delete()
        get_test.delete()
        return Response(status=200)


class StudentTestResultDeleteApiView(generics.DestroyAPIView):
    queryset = StudentTestResult.objects.all()
    serializer_class = StudentTestResultSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        test_id = instance.test.id
        get_test = StudentTest.objects.filter(id=test_id).first()
        student_results = StudentTestResult.objects.filter(test_id=test_id)
        student_results.delete()
        get_test.delete()
        return Response({"message": "Result muvaffaqiyatli o'chirildi"}, status=200)
