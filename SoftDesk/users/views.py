from django.contrib.auth import user_logged_in
from django.conf import settings

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer
from users.models import User


class CreateUserAPIView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthenticateUser(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.get(email=email, password=password)

            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)

                    user_details = {}
                    user_details['name'] = "%s %s" % (
                        user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    
                    return Response(user_details, status=status.HTTP_200_OK)
                
                except Exception as error:
                    raise error
            
            else:
                message = {'error': 'Vous ne pouvez pas être authentifié.'}
                return Response(message, status=status.HTTP_403_FORBIDDEN)
        
        except KeyError:
            message = {'error': 'Requiert un email et mot de passe.'}
            return Response(message)