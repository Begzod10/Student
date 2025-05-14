from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from users.models import Users
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
    user = request.user
    if request.user.is_superuser:
        stats_acceptedRequest = StudentRequest.objects.filter(request_status="acceptedRequest").aggregate(Count('id'))
        stats_rejectedRequest = StudentRequest.objects.filter(request_status="rejectedRequest").aggregate(Count('id'))
        stats_returnRequest = StudentRequest.objects.filter(request_status="returnRequest").aggregate(Count('id'))
        stats_newRequest = StudentRequest.objects.filter(request_status="newRequest").aggregate(Count('id'))
        stats = StudentRequest.objects.aggregate(Count('id'))
    else:
        stats_acceptedRequest = StudentRequest.objects.filter(Q(organization=user.organization_id) and
                                                              Q(request_status="acceptedRequest")).aggregate(
            Count('id'))
        stats_rejectedRequest = StudentRequest.objects.filter(Q(organization=user.organization_id) and
                                                              Q(request_status="rejectedRequest")).aggregate(
            Count('id'))
        stats_returnRequest = StudentRequest.objects.filter(Q(organization=user.organization_id) and
                                                            Q(request_status="returnRequest")).aggregate(Count('id'))
        stats_newRequest = StudentRequest.objects.filter(Q(organization=user.organization_id) and
                                                         Q(request_status="newRequest")).aggregate(Count('id'))
        stats = StudentRequest.objects.filter(Q(organization=user.organization_id)).aggregate(Count('id'))

    stats_with_extra_info = [
        {"accepted": {
            "count": stats_acceptedRequest,
            "text": "Qabul qilinganlar",
            "color": "#6188ECFF"
        }},
        {"back_recovery": {
            "count": stats_returnRequest,
            "text": "Tahrirlashgaqaytarilgan",
            "color": "#6188ECFF"
        }},
        {"canceled": {
            "count": stats_rejectedRequest,
            "text": "Rad etilgan",
            "color": "#6188ECFF"
        }},
        {"total_requests": {
            "count": stats,
            "text": "Barcha arizalar",
            "color": "#6188ECFF"
        }},
        {"new_requests": {
            "count": stats_newRequest,
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
