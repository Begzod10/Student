from django.urls import path

from users.user.api.crud.create import Register
from users.user.api.crud.update import UpdateUserInfo

urlpatterns = [
    path('', Register.as_view(), name='user-register'),
    path('<int:pk>/', UpdateUserInfo.as_view(), name='user-update'),
]
