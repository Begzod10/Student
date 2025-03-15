from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from students.models.student import StudentRequest
from students.serializers.student import StudentRequestSerializerList, StudentRequestSerializerRetrieve
from students.student_requests.filters import StudentRequestFilter


class StudentRequestListView(generics.ListAPIView):
    # Uncomment and use permissions as needed
    # permission_classes = [IsAuthenticated]

    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestSerializerList
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentRequestFilter

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            return StudentRequest.objects.filter(organization_id=organization_id)
        return StudentRequest.objects.all()


class StudentRequestRetrieveView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestSerializerRetrieve


@api_view(['GET'])
def student_request_dashboard(request):
    stats = StudentRequest.objects.aggregate(
        accepted_count=Count('id', filter=Q(accepted=True)),
        back_recovery_count=Count('id', filter=Q(back_recovery=True)),
        canceled_count=Count('id', filter=Q(canceled=True)),
        total_requests_count=Count('id'),
        new_requests_count=Count(
            'id',
            filter=Q(
                accepted=False,
                canceled=False,
                back_recovery=False,
                called_to_exam=False,
                present_in_exam=False,
                evaluated=False,
                contract_given=False,
                payed_status=False,
                accepted_to_study=False
            )
        )
    )

    stats_with_extra_info = [
        {"accepted": {
            "count": stats["accepted_count"],
            "text": "Qabul qilinganlar",
            "color": "#6188ECFF"
        }},
        {"back_recovery": {
            "count": stats["back_recovery_count"],
            "text": "Tahrirlashgaqaytarilgan",
            "color": "#6188ECFF"
        }},
        {"canceled": {
            "count": stats["canceled_count"],
            "text": "Rad etilgan",
            "color": "#6188ECFF"
        }},
        {"total_requests": {
            "count": stats["total_requests_count"],
            "text": "Barcha arizalar",
            "color": "#6188ECFF"
        }},
        {"new_requests": {
            "count": stats["new_requests_count"],
            "text": "Yangi kelib tushganlar",
            "color": "#6188ECFF"
        }},
        {"requests": {
            "count": 235345,
            "text": "Sahifaga tashrif buyuruvchilar",
            "color": "#6DEFC6FF"
        }},
    ]

    return Response(stats_with_extra_info)
