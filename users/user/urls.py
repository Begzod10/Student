from django.urls import path, include

urlpatterns = [
    path('user/crud/', include('users.user.api.crud.urls')),
    path('user/get/', include('users.user.api.get.urls')),

]
