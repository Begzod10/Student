from django.urls import path

from education.education.api.get.list import EducationList
from education.education.api.get.retriviev import EducationRetrieve

urlpatterns = [
    path('', EducationList.as_view(), name='education_list'),
    path('<int:pk>', EducationRetrieve.as_view(), name='education_retrieve'),
]
