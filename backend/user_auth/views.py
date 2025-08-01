
from django.contrib.auth import login,authenticate

from rest_framework.generics import GenericAPIView
from .models import UserAuth
from .serializers import UserRegistrationSerializer,UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class LoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self,*args,**kwargs):
        data = self.request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        user = authenticate(self.request, username=email,password = password) # To check for id and pass
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username
            }
        }, status=status.HTTP_200_OK)
class RegisterAPIView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self,*args,**kwargs):
        data = self.request.data
        email = data.get('email')
        existing_user = UserAuth.objects.filter(email = email).exists()
        if existing_user:
            return Response({'msg':'User Already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = UserRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'msg': 'User Created!',
            'refresh': str(refresh),
            'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        
        
