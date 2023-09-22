from django.contrib.auth import authenticate
from rest_framework import views, response, status, permissions
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from rest_framework.authtoken.models import Token


class RegisterAPI(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user).key
        return response.Response({'token': str(token)})


class LoginAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        email = self.request.data['email']
        password = self.request.data['password']
        if not User.objects.filter(email=email).first():
            return response.Response({"message": "Email does not exist!"}, status=status.HTTP_401_UNAUTHORIZED)
        if not authenticate(email=email, password=password):
            return response.Response({'message': 'Password incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.filter(email=email).first()
        token = Token.objects.get(user=user).key
        return response.Response({"token": str(token)})


class UserAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(instance=user, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'data': serializer.data})
