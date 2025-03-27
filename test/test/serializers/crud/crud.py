from rest_framework import serializers
from test.models.models import Test
from test.models.test_question import TestQuestion
from test.models.test_block import TestBlock
from organizations.models.organization_fields import OrganizationFields
from test.models.subject import Subject


class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'block', 'test', 'isTrue', 'answer', 'to_json']


class TestBlockSerializer(serializers.ModelSerializer):
    questions = TestQuestionSerializer(many=True)

    class Meta:
        model = TestBlock
        fields = ['id', 'test', 'text', 'to_json', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        block = TestBlock.objects.create(**validated_data)
        for question_data in questions_data:
            TestQuestion.objects.create(block=block, test=validated_data['test'], **question_data)
        return block


class TestCreateSerializer(serializers.ModelSerializer):
    blocks = TestBlockSerializer(many=True, required=False)

    class Meta:
        model = Test
        fields = ['id', 'name', 'field', 'subject', 'duration', 'blocks']

    def create(self, validated_data):
        print(validated_data)  # Debug uchun
        blocks_data = validated_data.pop('blocks', [])  # blocks ni validated_data ichidan olish
        print(blocks_data)  # Debug uchun

        test = Test.objects.create(**validated_data)

        for block_data in blocks_data:
            questions_data = block_data.pop('questions', [])
            block = TestBlock.objects.create(test=test, **block_data)

            for question_data in questions_data:
                TestQuestion.objects.create(block=block, test=test, **question_data)

        return test


class TestUpdateSerializer(serializers.ModelSerializer):
    blocks = TestBlockSerializer(many=True, required=False)

    class Meta:
        model = Test
        fields = ['name', 'subject', 'duration', 'blocks']

    def update(self, instance, validated_data):
        blocks_data = validated_data.pop('blocks', [])
        for block_data in blocks_data:
            questions_data = block_data.pop('questions', [])
            block, created = TestBlock.objects.get_or_create(test=instance, text=block_data['text'],
                                                             defaults=block_data)
            for question_data in questions_data:
                TestQuestion.objects.create(block=block, test=instance, **question_data)
        return super().update(instance, validated_data)
