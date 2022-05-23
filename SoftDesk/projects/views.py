from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import User
from projects.models import Projects, Contributors
from projects.serializers import ProjectSerializer, ContributorSerializer


class ProjectsViewset(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

    def list(self, request):
        queryset = Projects.objects.filter(author_user_id=self.request.user.id)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        project = request.data
        serializer = ProjectSerializer(data=project)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(author_user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def put (update or partial_update)
    # def delete (destroy)


class ContributorsViewset(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContributorSerializer
    queryset = Contributors.objects.all()

    def list(self, request, projects_pk=None):
        queryset = Contributors.objects.filter(project_id=projects_pk)
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, projects_pk=None):
        contributor = request.data
        serializer = ContributorSerializer(data=contributor)

        if serializer.is_valid(raise_exception=True):
            data = request.data
            user_to_add = User.objects.get(id=data['user_id'])
            current_project = Projects.objects.get(id=projects_pk)

            serializer.save(
                user = user_to_add,
                project = current_project,
                permission='CTB'
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, projects_pk=None, pk=None):
        contributor = Contributors.objects.filter(project=projects_pk, user=pk)

        if contributor:
            contributor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            message = 'Pas ou plus d`utilisateur à cette adresse'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
