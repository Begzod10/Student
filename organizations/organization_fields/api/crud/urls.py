from django.urls import path

from .delete import OrganizationFieldsDelete
from .update import OrganizationFieldsUpdate
from .create import OrganizationFieldsCreate

urlpatterns = [

    path('update/<int:pk>/', OrganizationFieldsUpdate.as_view(), name='organization-fields-update'),
    path('delete/<int:pk>/', OrganizationFieldsDelete.as_view(), name='organization-fields-delete'),
    path('create/', OrganizationFieldsCreate.as_view(), name='organization-fields-create'),
]
