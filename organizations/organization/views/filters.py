from rest_framework.response import Response
from rest_framework.decorators import api_view
from organizations.models import (
    OrganizationType,
    Organization,
    OrganizationFields,
    OrganizationDegrees,
)
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer
from organizations.organization_landing_page.serializers.get.retrieve_view import OrganizationLandingPageSerializer
from organizations.organization_fields.serializers.get.retrieve_view import OrganizationFieldsSerializer


@api_view(['GET'])
def organizations_filter(request, pk):
    try:
        organization_type = OrganizationType.objects.get(pk=pk)
        organizations = Organization.objects.filter(organization_type=organization_type)
        organization_fields = OrganizationFields.objects.filter(organization_type=organization_type)
        organization_degrees = OrganizationDegrees.objects.filter(organization_type=organization_type)

        fields_data = OrganizationFieldsSerializer(organization_fields, many=True).data
        degrees_data = OrganizationDegreesRetrieveSerializer(organization_degrees, many=True).data

        organizations_data = []
        for org in organizations:
            org_data = {

                'id': org.region.id,
                'name': org.region.name

            }
            organizations_data.append(org_data)

        languages = []
        for organization in organizations:
            # Use the correct field 'organization_id' instead of 'organization'
            landing_pages = OrganizationLandingPage.objects.filter(organization_id=organization.id)
            for landing_page in landing_pages:
                if landing_page.education_language:
                    languages.append({
                        'id': landing_page.education_language.id,
                        'name': landing_page.education_language.name,
                    })

        return Response({
            "organization_fields": fields_data,
            "organization_degrees": degrees_data,
            "region": organizations_data,
            "languages": languages,
        })

    except OrganizationType.DoesNotExist:
        return Response({"error": "OrganizationType not found"}, status=404)
    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=500)


@api_view(['POST'])
def organizations_get_filtereds(request):
    data = request.data
    organization_fields = data.get('organization_fields', [])
    organization_degrees = data.get('organization_degrees', [])
    landing_page_shrifts = data.get('landing_page_shrifts', [])
    languages = data.get('languages', [])
    region = data.get('region', [])
    landing_pages_qs = OrganizationLandingPage.objects.all()
    if organization_fields:
        landing_pages_qs = landing_pages_qs.filter(
            degree_id__organization_type__organizationfields__id__in=organization_fields
        )
    if organization_degrees:
        landing_pages_qs = landing_pages_qs.filter(
            degree_id__id__in=organization_degrees
        )
    if landing_page_shrifts:
        landing_pages_qs = landing_pages_qs.filter(
            landing_page_shift__id__in=landing_page_shrifts
        )
    if languages:
        landing_pages_qs = landing_pages_qs.filter(
            education_language__id__in=languages
        )
    if region:
        landing_pages_qs = landing_pages_qs.filter(
            organization_id__region__id__in=region
        )
    organization_landing_pages_data = OrganizationLandingPageSerializer(landing_pages_qs, many=True).data
    return Response({
        "organization_landing_pages": organization_landing_pages_data,
    })
