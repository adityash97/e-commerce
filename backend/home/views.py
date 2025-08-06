from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404
from .models import Cart
from user_auth.models import UserAuth
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import status
class CartGenericAPIView(GenericAPIView):
    """
    API View for Cart management on User Based
    """
    permission_classes=[IsAuthenticated]
    serializer_class = [CartSerializer]
    def get(self,request,*args,**kwargs):
        # TODO : check is user object or pk is coming or need to decode jtw token
        user = get_object_or_404(UserAuth,kwargs=kwargs.get('pk'))
        queryset = Cart.objects.filter(user = user)
        if queryset:
            serializer = CartSerializer(queryset,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({},status=status.HTTP_204_NO_CONTENT)

        
    def post(self,request,*args,**kwargs):
        pass


