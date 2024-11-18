from django.urls import path, include

urlpatterns = [
    path('user/crud/', include('Users.user.api.crud.urls')),
    path('user/get/', include('Users.user.api.get.urls')),

]
