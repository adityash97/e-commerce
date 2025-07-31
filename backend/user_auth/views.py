from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from .models import UserAuth
from .serializers import UserAuthSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class LoginAPIView(GenericAPIView):
    serializer_class = UserAuthSerializer
    def get(self,*args,**kwargs):
        data = self.request.data
        user = get_object_or_404(UserAuth,username =data.get('username'))
        #TODO: instead of returning user data send JWT Token
        serializer = UserAuthSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,*args,**kwargs):
        data = self.request.data
        email = data.get('email')
        existing_user = UserAuth.objects.filter(email = email).exists()
        if existing_user:
            return Response({'msg':'User Already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = UserAuthSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # TODO : also return token.
        return Response({'msg':'User Created!'},status=status.HTTP_200_OK)
        
        
