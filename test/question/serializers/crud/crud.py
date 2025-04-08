from rest_framework import serializers
from test.models.test_question import TestQuestion


class TestQuestionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = TestQuestion
        fields = ['id', 'block', 'test', 'isTrue', 'answer', 'to_json', 'image']
