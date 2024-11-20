from django.urls import path
from organizations.organization.api.get.retrieve_view import RetrieveOrganizationInfos
from django.urls import path, include

urlpatterns = [

    path('<int:pk>/', RetrieveOrganizationInfos.as_view(), name='user-retrieve'),
]
