from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from students.models.academic_year import AcademicYear
from students.academic_year.serializers.get.retrieve_view import AcademicYearRetrieveSerializer
from datetime import datetime


class AcademicYearListApiView(generics.ListAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearRetrieveSerializer
