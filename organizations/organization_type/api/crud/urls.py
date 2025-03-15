from django.urls import path

from .create import CreateOrganizationTypeView
from .update import UpdateOrganizationTypeView
from .delete import DeleteOrganizationTypeView

urlpatterns = [
    path('create/', CreateOrganizationTypeView.as_view()),
    path('update/<int:pk>/', UpdateOrganizationTypeView.as_view()),
    path('delete/<int:pk>/', DeleteOrganizationTypeView.as_view())
]
