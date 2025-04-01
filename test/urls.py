from django.urls import path, include

urlpatterns = [
    path('test/crud/', include('test.test.api.crud.urls')),
    path('test/get/', include('test.test.api.get.urls')),
    path('subject/get/', include('test.subject.api.get.urls')),
    path('block/crud/', include('test.block.api.crud.urls')),
    path('question/crud/', include('test.question.api.crud.urls')),

]
