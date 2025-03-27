from django.urls import path, include

urlpatterns = [
    path('test/crud/', include('test.test.api.crud.urls')),
]
