from django.urls import path
from .list import AcademicYearListApiView

urlpatterns = [
    path('', AcademicYearListApiView.as_view()),
]
