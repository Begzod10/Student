
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models.student import StudentRequest
from students.serializers.student import StudentRequestSerializerList, StudentRequestSerializerRetrieve
from rest_framework.decorators import api_view
from django.db.models import Count, Q


class StudentRequestListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestSerializerList


class StudentRequestRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestSerializerRetrieve


@api_view(['GET'])
def student_request_dashboard(request):

    stats = StudentRequest.objects.aggregate(
        accepted=Count('id', filter=Q(accepted=True)),
        back_recovery=Count('id', filter=Q(back_recovery=True)),
        canceled=Count('id', filter=Q(canceled=True)),
        total_requests=Count('id'),
        new_requests=Count(
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
    return Response(stats)

