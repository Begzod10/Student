from rest_framework import serializers
from test.models.models import Test, StudentTestResult
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock
from test.subject.serializers.get.get import SubjectSerializer
from organizations.organization_fields.serializers.get.retrieve_view import OrganizationFieldsSerializer
from organizations.organization_fields.serializers.get.list import OrganizationFieldsListSerializers


class TestQuestionSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'isTrue', 'answer', 'to_json', 'image']


class TestBlockSerializerGet(serializers.ModelSerializer):
    questions = TestQuestionSerializerGet(many=True, read_only=True)

    class Meta:
        model = TestBlock
        fields = ['id', 'text', 'to_json', 'questions', 'image']


class TestRetrieveSerializer(serializers.ModelSerializer):
    blocks = TestBlockSerializerGet(many=True, read_only=True)
    subject = SubjectSerializer(read_only=True)
    field_data = serializers.SerializerMethodField()
    number_questions = serializers.SerializerMethodField()

    def get_number_questions(self, obj):
        return TestBlock.objects.filter(test=obj).count() if obj else 0

    class Meta:
        model = Test
        fields = ['id', 'field', 'field_data', 'subject', 'duration', 'blocks', 'number_questions', 'is_mandatory',
                  'status']

    def get_field_data(self, obj):
        return [
            {
                "id": field.id,
                "name": field.name,
                "organization_type": {
                    "id": field.organization_type.id if field.organization_type else None,
                    "name": field.organization_type.name if field.organization_type else None
                }
            }
            for field in obj.field.all()
        ]


class TestListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    field = OrganizationFieldsListSerializers(read_only=True)
    field_data = serializers.SerializerMethodField()
    number_questions = serializers.SerializerMethodField()

    def get_number_questions(self, obj):
        return TestBlock.objects.filter(test=obj).count() if obj else 0

    class Meta:
        model = Test
        fields = ['id', 'field', 'field_data', 'subject', 'duration', 'number_questions', 'is_mandatory', 'status']

    def get_field_data(self, obj):
        return [
            {
                "id": field.id,
                "name": field.name,
                "organization_type": {
                    "id": field.organization_type.id if field.organization_type else None,
                    "name": field.organization_type.name if field.organization_type else None
                }
            }
            for field in obj.field.all()
        ]


class StudentTestResultSerializer(serializers.ModelSerializer):
    test = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    surname = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    # field = serializers.SerializerMethodField()
    # subject = serializers.SerializerMethodField()

    class Meta:
        model = StudentTestResult
        fields = ['test', 'result', 'true_answers', 'name', 'surname', 'id', 'date']

    def get_test(self, obj):
        if obj.test:
            test_obj = obj.test.test1 or obj.test.test2
            if test_obj:
                return {
                    'id': test_obj.id,
                    'duration': test_obj.duration,
                    'is_mandatory': test_obj.is_mandatory,
                    'subject': SubjectSerializer(test_obj.subject).data if test_obj.subject else None,
                    'field': [
                        {
                            "id": field.id,
                            "name": field.name,
                            "organization_type": {
                                "id": field.organization_type.id if field.organization_type else None,
                                "name": field.organization_type.name if field.organization_type else None
                            }
                        }
                        for field in test_obj.field.all()
                    ]

                }
        return None

    def get_name(self, obj):
        if obj.test:
            return obj.test.name
        return None

    def get_surname(self, obj):
        if obj.test:
            return obj.test.surname
        return None

    def get_date(self, obj):
        if obj.test:
            return obj.test.date.strftime("%Y-%m-%d")
        return None

    # def get_field(self, obj):
    #     if obj.test:
    #         test_obj = obj.test.test1 or obj.test.test2
    #         if test_obj:
    #             return obj.test_obj.field.name if obj.test_obj.field else None
    #     return None
    #
    # def get_subject(self, obj):
    #     if obj.test:
    #         test_obj = obj.test.test1 or obj.test.test2
    #         if test_obj:
    #             return obj.test_obj.subject.name if obj.test_obj.subject else None
    #     return None
