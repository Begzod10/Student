from django.urls import path

from users.user.api.crud.create import Register
from users.user.api.crud.update import UpdateUserInfo, UpdateUserPassword, UpdateUserPhoto

urlpatterns = [
    path('', Register.as_view(), name='user-register'),
    path('<int:pk>/', UpdateUserInfo.as_view(), name='user-update'),
    path('update_password/<int:pk>/', UpdateUserPassword.as_view(), name='user-password-update'),
    path('update_photo/<int:pk>/', UpdateUserPhoto.as_view(), name='user-photo-update'),
]
