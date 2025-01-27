from django.urls import path

from users.user.api.get.retirview import RetrieveUserInfos
from users.user.api.get.username_check import CheckCombinedAvailability

urlpatterns = [
    path('check-username/', CheckCombinedAvailability.as_view(), name='check-username'),

    path('<int:pk>/', RetrieveUserInfos.as_view(), name='user-retrieve'),
]
