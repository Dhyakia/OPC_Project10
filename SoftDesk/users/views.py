from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer


class CreateUserAPIView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
