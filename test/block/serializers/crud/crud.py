from rest_framework import serializers
from test.models.models import Test
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock
from pprint import pprint
import json


class TestQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'block', 'test', 'isTrue', 'answer', 'to_json', 'image']
        extra_kwargs = {'block': {'required': False}, 'test': {'required': False}}


class InlineTestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        exclude = ['block', 'test']  # ✅ We will set these manually in create/update


class TestBlockSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    questions_list = serializers.ListField(required=False, allow_null=True)
    questions = TestQuestionSerializers(many=True, read_only=True)

    class Meta:
        model = TestBlock
        fields = ['id', 'test', 'text', 'to_json', 'image', 'questions_list', 'questions']

    def create(self, validated_data):
        raw_questions = validated_data.pop('questions', [])
        image = validated_data.pop('image', None)
        block = TestBlock.objects.create(image=image, **validated_data)

        # Parse JSON string
        questions_data = json.loads(raw_questions[0]) if raw_questions else []

        for question_data in questions_data:
            TestQuestion.objects.create(block=block, test=block.test, **question_data)

        return block

    def update(self, instance, validated_data):
        raw_questions = validated_data.pop('questions_list', [])
        questions_data = json.loads(raw_questions[0]) if raw_questions else []
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        # Safely delete and recreate questions

        for question_data in questions_data:
            question_id = question_data.get('id') if 'id' in question_data else None
            if not question_id:
                TestQuestion.objects.create(
                    block=instance,
                    test=instance.test,
                    **question_data
                )
            else:
                question = TestQuestion.objects.get(id=question_id)
                question.answer = question_data['answer'] if 'answer' in question_data else None
                question.isTrue = question_data['isTrue']
                question.to_json = question_data['to_json']

                question.save()
        return instance
