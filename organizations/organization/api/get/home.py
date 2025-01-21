from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from organizations.models import Organization
from organizations.models.models import OrganizationGallery
from organizations.models.organization_landing_page import OrganizationAdvantage, OrganizationLandingPage
from organizations.organization.filters.home import OrganizationLandingPageFilter
from organizations.organization.serializers.get.retrieve_view import OrganizationDescSerializer, \
    OrganizationHomeSerializer, OrganizationAdvantagesSerializer, OrganizationGallerySerializer, \
    OrganizationOrganizationLandingPageSerializer, OrganizationOrganizationLandingPageSerializer2


class HomeOrganizationView(generics.ListAPIView):
    queryset = Organization.objects.filter(deleted=False).all()
    serializer_class = OrganizationHomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationLandingPageFilter


class HomeOrganizationRetrieveDescView(generics.RetrieveAPIView):
    serializer_class = OrganizationDescSerializer
    queryset = Organization.objects.all()


class HomeOrganizationRetrieveAdvantagesView(generics.RetrieveAPIView):
    serializer_class = OrganizationAdvantagesSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")

        return OrganizationAdvantage.objects.filter(organization_id=pk)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get()
        self.check_object_permissions(self.request, obj)
        return obj


class HomeOrganizationRetrieveGalleryView(generics.ListAPIView):
    serializer_class = OrganizationGallerySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        return OrganizationGallery.objects.filter(organization_id=pk)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get()
        self.check_object_permissions(self.request, obj)
        return obj


class HomeOrganizationRetrieveLandingPageDeegreeView(generics.ListAPIView):
    serializer_class = OrganizationOrganizationLandingPageSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        return OrganizationLandingPage.objects.filter(degree_id=pk)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get()
        self.check_object_permissions(self.request, obj)
        return obj


class ProfileLandingPageView(generics.RetrieveAPIView):
    serializer_class = OrganizationOrganizationLandingPageSerializer2
    queryset = OrganizationLandingPage.objects.all()
