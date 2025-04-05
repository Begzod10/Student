from rest_framework import serializers
from test.models.models import Test
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock


class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'block', 'test', 'isTrue', 'answer', 'to_json', 'image']
        extra_kwargs = {'block': {'required': False}, 'test': {'required': False}}


class TestBlockSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    questions = TestQuestionSerializer(many=True, required=False)

    class Meta:
        model = TestBlock
        fields = ['id', 'test', 'text', 'to_json', 'image', 'questions']

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        block = TestBlock.objects.create(image=image, **validated_data)
        return block

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for question_data in questions_data:
            TestQuestion.objects.create(block=instance, test=instance.test, **question_data)

        return instance
