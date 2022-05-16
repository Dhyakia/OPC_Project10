from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
