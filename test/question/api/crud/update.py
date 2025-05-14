from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from test.models.test_question import TestQuestion
from test.question.serializers.crud.crud import TestQuestionSerializer


class TestQuestionUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestQuestion.objects.all()
    serializer_class = TestQuestionSerializer
    parser_classes = (MultiPartParser, FormParser)

    def patch(self, request, *args, **kwargs):
        question = self.get_object()
        question.image = request.FILES.get('image', question.image)
        question.save()
        return Response(
            {"message": "Image updated successfully!", "image_url": question.image.url if question.image else None})

    def delete(self, request, *args, **kwargs):
        question = self.get_object()
        question.delete()
        return Response({"message": "Question deleted successfully!"}, status=200)
