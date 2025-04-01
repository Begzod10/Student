from rest_framework import status
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import NewsSerializer
from ..models.news import News, NewsView
from pprint import pprint
from django.utils.crypto import get_random_string


class NewsViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = News.objects.filter(deleted=False)
    serializer_class = NewsSerializer

    def create(self, request, *args, **kwargs):
        # Serializerdan foydalanish

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Frontenddan visitor_id ni olish
        visitor_id = request.headers.get('X-Visitor-ID')

        if not visitor_id or visitor_id in ('', 'null'):
            visitor_id = get_random_string(32)

        if not NewsView.objects.filter(news=instance, visitor_id=visitor_id).exists():
            NewsView.objects.create(news=instance, visitor_id=visitor_id)

        # Serializer context’ga visitor_id ni uzatish
        serializer = self.get_serializer(instance, context={'request': request, 'visitor_id': visitor_id})
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"message": "News deleted successfully."}, status=status.HTTP_200_OK)


class NewsViewOrganizationList(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return News.objects.filter(organization=organization_id, deleted=False)
