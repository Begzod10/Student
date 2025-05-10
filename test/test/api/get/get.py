import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from test.models.models import Test
from test.test.filtersets.testflter import TestFilter
from test.test.serializers.get.get import TestRetrieveSerializer, TestListSerializer
from test.models.test_block import TestBlock


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestRetrieveSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TestListApiView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TestFilter


class TestListApiViewForHome(APIView):
    def get(self, request):
        exclude_id = request.GET.get('id')
        tests = Test.objects.exclude(is_mandatory=True)
        if exclude_id:
            tests = tests.exclude(id=exclude_id)
        data = []
        for test in tests:
            data.append({
                'id': test.id,
                # 'name': test.name,
                'name': test.subject.name if test.subject else None,
                'duration': test.duration,
                'is_mandatory': test.is_mandatory,
            })
        return Response(data)

    def post(self, request):
        main_id = request.data.get("main_id")
        second_id = request.data.get("second_id")

        main_test = Test.objects.filter(id=main_id, is_mandatory=False).first()
        second_test = Test.objects.filter(id=second_id, is_mandatory=False).first()
        subject_names = ["ona tili", "matematika", "tarix"]
        mandatory_subjects = []
        total_duration = 0
        total_duration += main_test.duration if main_test else 0
        total_duration += second_test.duration if second_test else 0

        for subject_name in subject_names:
            tests = Test.objects.filter(is_mandatory=True, subject__name__icontains=subject_name)
            if tests.exists():
                selected = random.choice(tests)
                duration = selected.duration or 0
                total_duration += duration

                mandatory_subjects.append({
                    "subject": subject_name,
                    "test_id": selected.id,
                    "test_name": selected.name,
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
                "name": main_test.name if main_test else None,
                "question_count": TestBlock.objects.filter(test=main_test).count(),
                "duration": main_test.duration if main_test else 0,
            },
            "second_test": {
                "id": second_test.id if second_test else None,
                "name": second_test.name if second_test else None,
                "duration": second_test.duration if second_test else 0,
                "question_count": TestBlock.objects.filter(test=second_test).count()

            },
            "mandatory_tests": mandatory_subjects,
            "total_mandatory_duration": total_duration
        }

        return Response(response)
