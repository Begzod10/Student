from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Users


class CheckCombinedAvailability(APIView):
    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username')

        if not username :
            return Response({'error': 'At least one parameter (username or phone) is required'},
                            status=status.HTTP_400_BAD_REQUEST)

        username_exists = Users.objects.filter(username=username).exists() if username else False
        phone_exists = Users.objects.filter(phone=username).exists() if username else False

        if username_exists or phone_exists:
            return Response({'available': False, 'username_used': username_exists, 'phone_used': phone_exists},
                            status=status.HTTP_200_OK)

        return Response({'available': True}, status=status.HTTP_200_OK)
