from rest_framework.response import Response
from rest_framework.views import APIView

from ...serializers.get.sr_filter_items_for_organization_type import FilterItemsForOrganizationTypeSerializer


class FilterItemsForOrganizationTypeView(APIView):
    def get(self, request):
        type_id = request.query_params.get('type_id', None)
        serializer = FilterItemsForOrganizationTypeSerializer(context={'type_id': type_id})
        data = serializer.to_representation(None)
        return Response(data)
