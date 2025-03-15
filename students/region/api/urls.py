from django.urls import path, include

urlpatterns = [
    path('get/', include('students.region.api.get.urls')),
]
