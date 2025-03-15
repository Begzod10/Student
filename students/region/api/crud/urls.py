from django.urls import path

from students.region.api.crud.create import RegionCreateView
from students.region.api.crud.update import RegionUpdateView
from students.region.api.crud.destroy import RegionDeleteView

urlpatterns = [
    path('create/', RegionCreateView.as_view(), name='region-create'),
    path('update/<pk>/', RegionUpdateView.as_view(), name='region-update'),
    path('delete/<pk>/', RegionDeleteView.as_view(), name='region-delete'),
]
