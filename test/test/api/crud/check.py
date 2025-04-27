from collections import defaultdict

from rest_framework.response import Response
from rest_framework.views import APIView

from test.models.models import StudentTest, StudentTestResult, StudentTestResultAnswer, Test
from test.models.test_question import TestQuestion


class TestCheckView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        test_id = data.get('id')

        try:
            test = StudentTest.objects.get(id=test_id)
        except StudentTest.DoesNotExist:
            return Response({'error': 'StudentTest not found'}, status=404)

        mandatory_data = data.get('mandatory', [])
        optional_data = data.get('optional', [])

        correct_answer_ids = set(TestQuestion.objects.filter(isTrue=True).values_list('id', flat=True))

        total_score = 0
        result = StudentTestResult.objects.create(test=test, result=0, true_answers={})

        mandatory_scores = {}
        optional_scores = {}

        def get_subject_name(subject_id):
            subject = Test.objects.filter(pk=subject_id).first()
            return subject.subject.name if subject else f"Subject {subject_id}"

        def process_subject(subject_data, is_optional=False):
            nonlocal total_score
            subject_id = subject_data['subject_id']
            subject_name = get_subject_name(subject_id)
            subject_score = 0
            correct_count = 0

            is_test1 = test.test1 and test.test1.id == subject_id
            is_test2 = test.test2 and test.test2.id == subject_id

            for answer in subject_data['answers']:
                is_correct = answer['answer_id'] in correct_answer_ids
                if is_correct:
                    correct_count += 1
                    if not is_optional:
                        subject_score += 1.1
                        total_score += 1.1


                    else:
                        if is_test1:
                            subject_score += 3.1
                            total_score += 3.1

                        elif is_test2:
                            subject_score += 2.1
                            total_score += 2.1

                savet = StudentTestResultAnswer.objects.create(
                    result=result,
                    question_id=answer['question_block_id'],
                    answer_id=answer['answer_id'],
                    is_true=is_correct
                )

            return {
                'score': round(subject_score, 2),
                'correct_count': correct_count,
                'subject': subject_name
            }

        for subject in mandatory_data:
            score_data = process_subject(subject, is_optional=False)
            mandatory_scores[score_data['subject']] = score_data

        for subject in optional_data:
            score_data = process_subject(subject, is_optional=True)
            optional_scores[score_data['subject']] = score_data

        result.true_answers = {
            'mandatory': mandatory_scores,
            'optional': optional_scores,
            'total_score': round(total_score, 2)
        }
        result.result = round(total_score, 2)
        result.save()

        return Response({
            'id': test_id,
            'status': 'ok',
            'mandatory': mandatory_scores,
            'optional': optional_scores,
            'total_score': round(total_score, 2)
        })

    def get(self, request, *args, **kwargs):
        test_id = request.query_params.get('id')
        if not test_id:
            return Response({'error': 'StudentTest ID is required'}, status=400)

        try:
            student_test = StudentTest.objects.get(id=test_id)
        except StudentTest.DoesNotExist:
            return Response({'error': 'StudentTest not found'}, status=404)

        result = StudentTestResult.objects.filter(test=student_test).first()
        if not result:
            return Response({'error': 'Result not found for this test'}, status=404)

        answers = StudentTestResultAnswer.objects.filter(result=result)

        test1_id = student_test.test1.id if student_test.test1 else None
        test2_id = student_test.test2.id if student_test.test2 else None

        subjects_grouped = defaultdict(list)

        for ans in answers:
            if not ans.question or not ans.answer:
                continue

            block = ans.question
            test_block = block.test
            subject = test_block.subject if test_block else None
            subject_name = subject.name if subject else "Unknown"
            subject_type = "optional" if test_block and test_block.id in [test1_id, test2_id] else "mandatory"

            options = TestQuestion.objects.filter(block=block)

            answer_options = []
            for opt in options:
                answer_options.append({
                    "id": opt.id,
                    "answer": opt.answer,
                    "to_json": opt.to_json,
                    "image": opt.image.url if opt.image else None,
                    "is_selected": (opt.id == ans.answer_id),
                    "is_true": opt.isTrue
                })

            question_data = {
                "id": block.id,
                "text": block.text,
                "to_json": block.to_json,
                "image": block.image.url if block.image else None,
                "is_true": ans.is_true,

                "answer_options": answer_options
            }

            subjects_grouped[(subject_name, subject_type)].append(question_data)

        response_subjects = [{
            "name": subject_name,
            "type": subject_type,
            "questions": questions
        } for (subject_name, subject_type), questions in subjects_grouped.items()]

        return Response({
            "student_test_id": student_test.id,
            "score": result.result,
            "subjects": response_subjects,
            "info": result.true_answers
        })
