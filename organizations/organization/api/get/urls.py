from django.urls import path

from organizations.organization.api.get.filter_for_type import FilterForTypeOrganizationView
from organizations.organization.api.get.home import HomeOrganizationView, HomeOrganizationRetrieveDescView, \
    HomeOrganizationRetrieveAdvantagesView, HomeOrganizationRetrieveGalleryView, \
    HomeOrganizationRetrieveLandingPageDeegreeView, ProfileLandingPageView
from organizations.organization.api.get.retrieve_view import RetrieveOrganizationInfos
from organizations.organization.views.filters import organizations_filter, organizations_get_filtereds

urlpatterns = [
    path('<int:pk>/', RetrieveOrganizationInfos.as_view(), name='user-retrieve'),
    path('organizations_filter/<int:pk>/', organizations_filter, name='organizations-filter'),
    path('organizations_get_filtereds/', organizations_get_filtereds, name='organizations-filter'),
    path('filter_for_type/', FilterForTypeOrganizationView.as_view(), name='filter_for_type'),
    path('filter_for_type/', FilterForTypeOrganizationView.as_view(), name='filter_for_type'),
    path('home/', HomeOrganizationView.as_view(), name='filter_for_type'),
    path('home/desc/<int:pk>/', HomeOrganizationRetrieveDescView.as_view(), name='filter_for_type'),
    path('home/advantages/<int:pk>/', HomeOrganizationRetrieveAdvantagesView.as_view(), name='filter_for_type'),
    path('home/gallary/<int:pk>/', HomeOrganizationRetrieveGalleryView.as_view(), name='filter_for_type'),
    path('home/degree/<int:pk>/', HomeOrganizationRetrieveLandingPageDeegreeView.as_view(), name='filter_for_type'),
    path('home/landing/<int:pk>/', ProfileLandingPageView.as_view(), name='filter_for_type'),
    path('organizations_filter/<int:pk>/', organizations_filter, name='organizations-filter'),
    path('organizations_get_filtereds/', organizations_get_filtereds, name='organizations-filter'),

]
