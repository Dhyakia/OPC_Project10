from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import User
from projects.models import Projects, Contributors, Issues
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer


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
            user_to_add = User.objects.get(id=contributor['user_id'])
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
            return Response(message, status=status.HTTP_404_NOT_FOUND)


class IssuesViewset(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IssueSerializer
    queryset = Issues.objects.all()

    def list(self, request, projects_pk=None):
        queryset = Issues.objects.filter(project=projects_pk)
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, projects_pk=None):
        issue = request.data
        serializer = IssueSerializer(data=issue)

        if serializer.is_valid(raise_exception=True):
            author = User.objects.get(id=request.user.id)
            assigne = User.objects.get(id=issue['assigne_user'])
            current_project = Projects.objects.get(id=projects_pk)

            serializer.save(
                author_user = author,
                assigne_user = assigne,
                project = current_project
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, projects_pk=None, pk=None):
        issue = Issues.objects.filter(project=projects_pk, id=pk)

        if issue:
            issue.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            message = 'Pas ou plus de problême à cette adresse'
            return Response(message, status=status.HTTP_404_NOT_FOUND)