from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from organizations.models import Organization
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.filters.home import OrganizationLandingPageFilter
from organizations.organization.serializers.get.retrieve_view import OrganizationDescSerializer, \
    OrganizationHomeSerializer


class HomeOrganizationView(generics.ListAPIView):
    queryset = OrganizationLandingPage.objects.filter(deleted=False).all()
    serializer_class = OrganizationHomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationLandingPageFilter


class HomeOrganizationRetrieveDescView(generics.RetrieveAPIView):
    serializer_class = OrganizationDescSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")

        landing_page = get_object_or_404(OrganizationLandingPage, pk=pk)

        return Organization.objects.filter(id=landing_page.organization_id, deleted=False)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get()
        self.check_object_permissions(self.request, obj)
        return obj
