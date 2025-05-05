from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from students.models.student import StudentRequest
from students.student_requests.serializers.crud.crud import StudentRequestCreateUpdateSerializer2
from organizations.models.organization_landing_page import OrganizationLandingPage
from rest_framework.response import Response
from rest_framework import status
from students.models.student import StudentRequest, Student, Shift


class StudentRequestCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentRequest.objects.all().select_related(
        'student__user', 'degree', 'shift', 'language', 'organization__organization_type', 'organization__region'
    )
    serializer_class = StudentRequestCreateUpdateSerializer2

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        landing_id = request.data.get('landing')

        if not user_id or not landing_id:
            return Response({"detail": "Foydalanuvchi yoki Landing topilmadi."}, status=status.HTTP_400_BAD_REQUEST)

        # Now, manually check conditions
        student = get_object_or_404(Student, user=user_id)
        user = student.user

        if not (user.passport_seria and user.passport_pdf1 and user.passport_pdf2 and user.name and user.surname):
            return Response({"detail": "Profil ma'lumotlari yetarli emas!", "status": False}, status=status.HTTP_200_OK)

        landing_page = get_object_or_404(OrganizationLandingPage, id=landing_id)

        if StudentRequest.objects.filter(
                student=student,
                field=landing_page.field,
                landing_page=landing_page,
        ).exists():
            return Response({"detail": "Siz allaqachon bu yo'nalishdan ro'yhatdan o'tgansiz!"},
                            status=status.HTTP_200_OK)

        # All good — now use serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Arizangiz topshirildi!", "status": True}, status=status.HTTP_201_CREATED,
                        headers=headers)
