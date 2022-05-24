from rest_framework import serializers

from projects.models import Projects, Contributors, Issues


class ProjectSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Projects
        fields = ('id', 'title', 'description', 'type', 'author_user_id')
        read_only_fields = ['author_user_id']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Contributors
        fields = ('id', 'user', 'project', 'permission', 'role')
        read_only_fields = ['user', 'project']


class IssueSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Issues
        fields = ('id', 'title', 'desc', 'priority', 'tag', 'author_user', 'assigne_user', 'project')
        read_only_fields = ['author_user', 'assigne_user', 'project']