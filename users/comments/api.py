from rest_framework import generics
from django.db.models import Avg
from rest_framework.response import Response
from users.comments.serializers import CommentSerializer
from users.models import Comments, Users
from organizations.models import Organization
from pprint import pprint


class CommentCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        user = Users.objects.get(id=request.data['user']) if 'user' in request.data else None
        organization = Organization.objects.get(
            id=request.data['organization']) if 'organization' in request.data else None
        create_comment = Comments.objects.create(
            comment=request.data['comment'],
            rating=request.data['rating'],
            organization=organization,
            name=request.data['name'] if 'name' in request.data else None,
            surname=request.data['surname'] if 'surname' in request.data else None,
            user=user)
        average_rating = Comments.objects.filter(organization=request.data['organization']).aggregate(Avg('rating'))[
            'rating__avg']
        get_organization = Organization.objects.get(id=request.data['organization'])
        get_organization.rating = average_rating
        get_organization.save()

        return Response({'comment': CommentSerializer(create_comment).data})



class CommentListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id')
        if organization_id:
            return Comments.objects.filter(organization=organization_id)
        return Comments.objects.none()  # Or return all comments if you prefer
