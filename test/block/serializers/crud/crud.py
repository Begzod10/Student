from rest_framework import serializers
from test.models.models import Test
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock


class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'block', 'test', 'isTrue', 'answer', 'to_json']


class TestBlockSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = TestBlock
        fields = ['id', 'test', 'text', 'to_json', 'image']

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        block = TestBlock.objects.create(image=image, **validated_data)
        return block
