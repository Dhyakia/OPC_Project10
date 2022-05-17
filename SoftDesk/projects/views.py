from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from projects.models import Projects
from projects.serializers import ProjectSerializer


class ProjectsViewset(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

    def get_queryset(self):
        # TODO: Filtrer les contributeurs
        queryset = self.queryset
        query_filtered = queryset.filter(author_user_id=self.request.user.id)
        return query_filtered

    def create(self, request):
        project = request.data
        serializer = ProjectSerializer(data=project)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(author_user_id=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
