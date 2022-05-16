from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from projects.serializers import ProjectSerializer


class ProjectAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Récupérer les projects dont l'utilisateur est:
        # 1. l'auteur
        # 2. Un contributeur
        
        return Response()

    def post(self, request):
        project = request.data
        serializer = ProjectSerializer(data=project)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(author_user_id=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)