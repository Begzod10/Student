from rest_framework import serializers
from test.models.models import Test
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock
from test.subject.serializers.get.get import SubjectSerializer
from organizations.organization_fields.serializers.get.list import OrganizationFieldsListSerializers


class TestQuestionSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'isTrue', 'answer', 'to_json']


class TestBlockSerializerGet(serializers.ModelSerializer):
    questions = TestQuestionSerializerGet(many=True, read_only=True)

    class Meta:
        model = TestBlock
        fields = ['id', 'text', 'to_json', 'questions']


class TestRetrieveSerializer(serializers.ModelSerializer):
    blocks = TestBlockSerializerGet(many=True, read_only=True)
    subject = SubjectSerializer(read_only=True)
    field = OrganizationFieldsListSerializers(read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'name', 'field', 'subject', 'duration', 'blocks']


class TestListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    field = OrganizationFieldsListSerializers(read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'name', 'field', 'subject', 'duration']
