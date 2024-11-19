from django.urls import path

from users.user.api.get.retirview import RetrieveUserInfos

urlpatterns = [
    path('<int:pk>/', RetrieveUserInfos.as_view(), name='user-retrieve'),
]
