from django.urls import include,path

urlpatterns = [
    path('get/', include('students.shift.api.get.urls')),
]