from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import User
from projects.models import Projects, Contributors, Issues, Comments
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


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
        return Response(serializer.data, status=status.HTTP_200_OK)

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


class CommentsViewset(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def list(self, request, projects_pk=None, issues_pk=None):
        queryset = Comments.objects.filter(issue=issues_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, projects_pk=None, issues_pk=None):
        comment = request.data
        serializer = CommentSerializer(data=comment)

        if serializer.is_valid(raise_exception=True):
            current_user = User.objects.get(id=request.user.id)
            current_issue = Issues.objects.get(id=issues_pk, project=projects_pk)

            serializer.save(
                author_user = current_user,
                issue = current_issue
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, projects_pk=None, issues_pk=None, pk=None):   
        current_user = User.objects.get(id=request.user.id)
        current_issue = Issues.objects.get(id=issues_pk, project=projects_pk)

        comment = Comments.objects.filter(
            author_user=current_user,
            issue=current_issue,
            id=pk
            )

        if comment:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            message = 'Pas ou plus de commentaire à cette adresse'
            return Response(message, status=status.HTTP_404_NOT_FOUND)

# TODO: fonction list ne filtre pas suffisement, je crois
# TODO: la 19eme function à écrire