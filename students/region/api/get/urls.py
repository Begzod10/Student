from django.urls import path

from students.region.api.get.list import RegionListView, DistrictListView
from students.region.api.get.retrieve import RegionRetrieveView

urlpatterns = [
    path('<int:pk>/', RegionRetrieveView.as_view(), name='region-retrieve'),
    path('', RegionListView.as_view(), name='region-list'),
    path('list_district/', DistrictListView.as_view(), name='district-list'),
]
