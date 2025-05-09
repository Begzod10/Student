from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from organizations.models import Organization
from organizations.models.models import OrganizationGallery
from organizations.models.organization_landing_page import OrganizationAdvantage, OrganizationLandingPage
from organizations.organization.filters.home import OrganizationLandingPageFilter
from organizations.organization.serializers.get.retrieve_view import OrganizationDescSerializer, \
    OrganizationHomeSerializer, OrganizationAdvantagesSerializer, OrganizationGallerySerializer, \
    OrganizationOrganizationLandingPageSerializer, OrganizationOrganizationLandingPageSerializer2


class HomeOrganizationView(generics.ListAPIView):
    queryset = Organization.objects.filter(deleted=False).distinct()
    serializer_class = OrganizationHomeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = OrganizationLandingPageFilter
    search_fields = [
        'name',
        '^name',
        '=name',
    ]


class HomeOrganizationRetrieveDescView(generics.RetrieveAPIView):
    serializer_class = OrganizationDescSerializer
    queryset = Organization.objects.all()


class HomeOrganizationRetrieveAdvantagesView(generics.RetrieveAPIView):
    serializer_class = OrganizationAdvantagesSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return OrganizationAdvantage.objects.none()
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
        if getattr(self, 'swagger_fake_view', False):
            return OrganizationGallery.objects.none()
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
        if getattr(self, 'swagger_fake_view', False):
            return Organization.objects.none()
        pk = self.kwargs.get('pk')
        if pk is None:
            raise KeyError("'pk' not found in URL kwargs.")
        return OrganizationLandingPage.objects.filter(degree_id=pk,deleted=False)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get()
        self.check_object_permissions(self.request, obj)
        return obj


class ProfileLandingPageView(generics.RetrieveAPIView):
    serializer_class = OrganizationOrganizationLandingPageSerializer2
    queryset = OrganizationLandingPage.objects.all()


class HomeOrganizationCombinedView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            response_data = {
                'description': self.get_description(pk),
                'advantages': self.get_advantages(pk),
                'gallery': self.get_gallery(pk),
                'degree': self.get_degree(pk),
                'landing': self.get_landing(pk),
            }
            return Response(response_data)
        except Exception as e:
            raise Http404(f"Error retrieving data: {str(e)}")

    def get_description(self, organization_id):
        try:
            obj = Organization.objects.get(id=organization_id)
            serializer = OrganizationDescSerializer(obj)
            return serializer.data
        except Organization.DoesNotExist:
            return None

    def get_advantages(self, organization_id):
        queryset = OrganizationAdvantage.objects.filter(organization_id=organization_id)
        if not queryset.exists():
            return []
        serializer = OrganizationAdvantagesSerializer(queryset, many=True)
        return serializer.data

    def get_gallery(self, organization_id):
        queryset = OrganizationGallery.objects.filter(organization_id=organization_id)
        if not queryset.exists():
            return []
        serializer = OrganizationGallerySerializer(queryset, many=True)
        return serializer.data

    def get_degree(self, organization_id):
        queryset = OrganizationLandingPage.objects.filter(organization_id=organization_id,deleted=False)
        if not queryset.exists():
            return []
        serializer = OrganizationOrganizationLandingPageSerializer(queryset, many=True)
        return serializer.data

    def get_landing(self, organization_id):
        try:
            obj = OrganizationLandingPage.objects.filter(organization_id=organization_id,deleted=False)
            serializer = OrganizationOrganizationLandingPageSerializer2(obj, many=True)
            return serializer.data
        except OrganizationLandingPage.DoesNotExist:
            return None
