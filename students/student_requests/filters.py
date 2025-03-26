import django_filters

from students.models.student import StudentRequest


class StudentRequestFilter(django_filters.FilterSet):
    type_id = django_filters.NumberFilter(field_name="organization__organization_type_id")

    degree_id = django_filters.NumberFilter(field_name="degree_id")
    language_id = django_filters.NumberFilter(field_name="language_id")
    shift_id = django_filters.NumberFilter(field_name="shift_id")
    field_id = django_filters.NumberFilter(field_name="field_id")
    status = django_filters.CharFilter(method='filter_status')
    student_id = django_filters.NumberFilter(field_name='student_id')

    class Meta:
        model = StudentRequest
        fields = ['degree_id', 'language_id', 'type_id', 'shift_id', 'field_id', 'status', 'student_id']

    def filter_status(self, queryset, name, value):

        if value == 'rejectedRequest':
            return queryset.filter(request_status='rejectedRequest')
        elif value == 'allRequest':
            return queryset  # Returning the full queryset is valid
        elif value == 'acceptedRequest':
            return queryset.filter(request_status='acceptedRequest')
        elif value == 'returnRequest':
            return queryset.filter(request_status='returnRequest')
        elif value == 'invitedRequest':
            return queryset.filter(request_status='invitedRequest')
        elif value == 'newRequest':
            return queryset.filter(
                canceled=False, accepted=False, back_recovery=False, called_to_exam=False
            )

        return queryset.none()
