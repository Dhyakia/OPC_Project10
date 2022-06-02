from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from projects.models import Projects, Contributors, Issues, Comments
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

    def list(self, request):
        # perm: all authenticated
        query_author = Projects.objects.filter(author_user=self.request.user.id)
        serializer_author = ProjectSerializer(query_author, many=True)

        query_contrib = Contributors.objects.filter(user_id=self.request.user.id)
        serializer_contrib = ContributorSerializer(query_contrib, many=True)

        return Response({
            'author': serializer_author.data,
            'contributor': serializer_contrib.data,
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # perm: project author and contrib
        current_user = self.request.user.id

        if Projects.objects.filter(id=pk, author_user=current_user).exists() or Contributors.objects.filter(project_id=pk, user_id=current_user).exists():
            query = Projects.objects.get(id=pk)
            serializer = ProjectSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            message = 'Circulez, rien à voir'
            return Response(message, status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        # perm: all authenticated
        project = request.data
        serializer = ProjectSerializer(data=project)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(author_user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        # perm: project author only
        current_user = self.request.user.id

        if Projects.objects.filter(id=pk, author_user=current_user).exists():
            new_title = request.data['title']
            new_description = request.data['description']
            new_type = request.data['type']

            project = Projects.objects.filter(id=pk).update(
                title=new_title,
                description=new_description,
                type=new_type
                )

            return Response(status=status.HTTP_202_ACCEPTED)

        else:
            message = 'Circulez, rien à voir'
            return Response(message, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # perm: project author only
        current_user = self.request.user.id
        
        if Projects.objects.filter(id=pk, author_user=current_user).exists():
            project = Projects.objects.filter(id=pk)
            if project.exists():
                project.delete()            
                return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                message = 'Pas ou plus de projet à cette adresse'
                return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        else:
            message = 'Circulez, rien à voir'
            return Response(message, status=status.HTTP_403_FORBIDDEN)


class ContributorsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer
    queryset = Contributors.objects.all()

    def list(self, request, projects_pk=None):
        # Perm: project author & contrib
        current_user = self.request.user.id

        if Projects.objects.filter(id=projects_pk, author_user=current_user).exists() or Contributors.objects.filter(project_id=projects_pk, user_id=current_user).exists():
            query_author = Projects.objects.filter()
            serizalizer_author = 

            query_contrib = Contributors.objects.filter(project_id=projects_pk)
            serializer_contrib = ContributorSerializer(query_contrib, many=True)
            return Response({
                'author': serizalizer_author.data,
                'contributors': serializer_contrib.data,
            }, status=status.HTTP_200_OK)
        
        else:
            message = 'Circulez, rien à voir'
            return Response(message, status=status.HTTP_403_FORBIDDEN)
    
    def create(self, request, projects_pk=None):
        # Perm: project author
        current_user = self.request.user.id

        if Projects.objects.filter(id=projects_pk, author_user=current_user).exists():
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

            else:
                message = 'Serializer ne passe pas la validation'
                return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            message = 'Circulez, rien à voir'
            return Response(message, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, projects_pk=None, pk=None):
        # Perm: project author
        current_user = self.request.user.id

        if Projects.objects.filter(id=projects_pk, author_user=current_user).exists():
            contributor = Contributors.objects.filter(id=pk)
            if contributor.exists():
                contributor.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                message = 'Pas ou plus d`utilisateur à cette adresse'
                return Response(message, status=status.HTTP_404_NOT_FOUND)

        else:
            message = 'Circulez, rien à voir'
            return Response(message, status=status.HTTP_403_FORBIDDEN)    


class IssuesViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
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

    def update(self, request, projects_pk=None, pk=None):
        new_title = request.data['title']
        new_desc = request.data['desc']
        new_priority = request.data['priority']
        new_tag = request.data['tag']

        issue = Issues.objects.filter(id=pk).update(
            title=new_title,
            desc=new_desc,
            priority=new_priority,
            tag=new_tag
        )

        return Response(status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, projects_pk=None, pk=None):
        issue = Issues.objects.filter(project=projects_pk, id=pk)

        if issue.exists():
            issue.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            message = 'Pas ou plus de problême à cette adresse'
            return Response(message, status=status.HTTP_404_NOT_FOUND)


class CommentsViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def list(self, request, projects_pk=None, issues_pk=None):
        queryset = Comments.objects.filter(issue=issues_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, projects_pk=None, issues_pk=None, pk=None):
        query =  Comments.objects.get(id=pk)
        serializer = CommentSerializer(query)
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

    def update(self, request, projects_pk=None, issues_pk=None, pk=None):
        new_description = request.data['description']
        comment = Comments.objects.filter(id=pk).update(
            description=new_description
        )

        return Response(status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, projects_pk=None, issues_pk=None, pk=None):
        current_user = User.objects.get(id=request.user.id)
        current_issue = Issues.objects.get(id=issues_pk, project=projects_pk)

        comment = Comments.objects.filter(
            author_user=current_user,
            issue=current_issue,
            id=pk
            )

        if comment.exists():
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            message = 'Pas ou plus de commentaire à cette adresse'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
