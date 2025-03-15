from django.urls import path,include
urlpatterns = [
    path('get/', include('education.education.api.get.urls')),
]