from django.urls import path

from Users.user.api.get.retirview import RetrieveUserInfos

urlpatterns = [
    path('<int:pk>/', RetrieveUserInfos.as_view(), name='user-retrieve'),
]
