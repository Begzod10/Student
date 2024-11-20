from rest_framework import serializers

from organizations.models.models import OrganizationDegrees, OrganizationType
from organizations.models.organization_fields import OrganizationFields
from students.models.student import Shift
from education.models import EducationLanguage


class FilterItemsForOrganizationTypeSerializer(serializers.Serializer):

    def to_representation(self, obj):
        type_id = self.context.get('type_id', None)
        types = OrganizationType.objects.all()
        if type_id:
            degrees = OrganizationDegrees.objects.filter(organization_type_id=type_id).all()
            fields = OrganizationFields.objects.filter(organization_type_id=type_id).all()
            shifts = Shift.objects.filter(organization_type_id=type_id).all()
            languages = EducationLanguage.objects.all()
            return {
                'degrees': [{'id': degree.id, 'name': degree.name} for degree in degrees],
                'fields': [{'id': field.id, 'name': field.name} for field in fields],
                'shifts': [{'id': shift.id, 'name': shift.name} for shift in shifts],
                'languages': [{'id': language.id, 'name': language.name} for language in languages]
            }
        return {'types': [{'id': type.id, 'name': type.name} for type in types]}
