from rest_framework import serializers
from test.models.models import Test
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock
from test.subject.serializers.get.get import SubjectSerializer
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
        fields = ['id', 'field', 'field_data', 'subject', 'duration', 'blocks', 'number_questions', 'is_mandatory']

    def get_field_data(self, obj):
        return {
            "id": obj.field.id,
            "name": obj.field.name,
            "organization_type": {
                "id": obj.field.organization_type.id,
                "name": obj.field.organization_type.name
            }
        }


class TestListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    field = OrganizationFieldsListSerializers(read_only=True)
    number_questions = serializers.SerializerMethodField()

    def get_number_questions(self, obj):
        return TestBlock.objects.filter(test=obj).count() if obj else 0

    class Meta:
        model = Test
        fields = ['id', 'field', 'subject', 'duration', 'number_questions']
