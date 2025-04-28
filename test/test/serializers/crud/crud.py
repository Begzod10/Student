import pprint
import random

from rest_framework import serializers

from test.block.serializers.crud.crud import TestBlockSerializer
from test.models.models import StudentTest
from test.models.models import Test
from test.models.test_block import TestBlock
from test.models.test_question import TestQuestion


class TestCreateSerializer(serializers.ModelSerializer):
    blocks = TestBlockSerializer(many=True, required=False)

    class Meta:
        model = Test
        fields = ['id', 'name', 'field', 'subject', 'duration', 'blocks', 'is_mandatory']

    def create(self, validated_data):
        blocks_data = validated_data.pop('blocks', [])

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
        fields = ['id', 'name', 'field', 'subject', 'duration', 'blocks', 'is_mandatory']

    def update(self, instance, validated_data):
        pprint.pprint(validated_data)
        blocks_data = validated_data.pop('blocks', [])
        for block_data in blocks_data:
            questions_data = block_data.pop('questions', [])
            block, created = TestBlock.objects.get_or_create(test=instance, text=block_data['text'],
                                                             defaults=block_data)
            for question_data in questions_data:
                TestQuestion.objects.create(block=block, test=instance, **question_data)
        return super().update(instance, validated_data)


class StudentTestSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField(read_only=True)
    questions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StudentTest
        fields = '__all__'

    def validate(self, data):
        student = data.get('student')
        name = data.get('name')
        surname = data.get('surname')

        if not student and not (name and surname):
            raise serializers.ValidationError(
                "Agar student yo'q bo‘lsa, name va surname bo‘lishi kerak."
            )
        return data

    def get_subject(self, obj):
        return [
            {
                'id': obj.test1.subject.id,
                'name': obj.test1.subject.name,
                'question_count': 30
            },
            {
                'id': obj.test2.subject.id if obj.test2.subject else None,
                'name': obj.test2.subject.name if obj.test2.subject else None,
                'question_count': 30

            }
        ]

    def get_questions(self, obj):
        data = {
            'mandatory': [],
            'optional': []
        }

        mandatory_tests = list(Test.objects.filter(is_mandatory=True).exclude(id__in=[obj.test1_id, obj.test2_id]))
        selected_mandatory_tests = random.sample(mandatory_tests, min(3, len(mandatory_tests)))

        for test in selected_mandatory_tests:
            test_data = {
                'id': test.id,
                'name': test.subject.name if test.subject else None,
                'duration': test.duration,
                'is_mandatory': test.is_mandatory,
                'subject_id': test.subject_id,
                'field_id': test.field_id,
                'question_count': TestBlock.objects.filter(test=test).count(),
                'blocks': []
            }

            for block in TestBlock.objects.filter(test=test):
                block_data = {
                    'id': block.id,
                    'text': block.text,
                    'to_json': block.to_json,
                    'image': block.image.url if block.image else None,
                    'questions': []
                }

                for question in TestQuestion.objects.filter(block=block):
                    question_data = {
                        'id': question.id,
                        'answer': question.answer,
                        'isTrue': question.isTrue,
                        'to_json': question.to_json,
                        'image': question.image.url if question.image else None
                    }
                    block_data['questions'].append(question_data)

                test_data['blocks'].append(block_data)

            data['mandatory'].append(test_data)

        for test in [obj.test1, obj.test2]:
            if not test:
                continue

            test_data = {
                'id': test.id,
                'name': test.subject.name if test.subject else None,
                'duration': test.duration,
                'is_mandatory': test.is_mandatory,
                'subject_id': test.subject_id,
                'field_id': test.field_id,
                'question_count': TestBlock.objects.filter(test=test).count(),

                'blocks': []
            }

            for block in TestBlock.objects.filter(test=test):
                block_data = {
                    'id': block.id,
                    'text': block.text,
                    'to_json': block.to_json,
                    'image': block.image.url if block.image else None,
                    'questions': []
                }

                for question in TestQuestion.objects.filter(block=block):
                    question_data = {
                        'id': question.id,
                        'answer': question.answer,
                        'isTrue': question.isTrue,
                        'to_json': question.to_json,
                        'image': question.image.url if question.image else None
                    }
                    block_data['questions'].append(question_data)

                test_data['blocks'].append(block_data)

            data['optional'].append(test_data)

        return data
