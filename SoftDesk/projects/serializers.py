from rest_framework import serializers

from projects.models import Projects


class ProjectSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Projects
        fields = ('id', 'title', 'description', 'type', 'author_user_id')
