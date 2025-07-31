from rest_framework import serializers
from .models import UserAuth
class UserAuthSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(allow_blank=False,write_only=True)
    password = serializers.CharField(allow_blank=False,write_only=True)
    class Meta:
        model = UserAuth
        exclude=('groups',)
        extra_kwargs = {
            'username':{'required':False,'allow_blank':True}
        }
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Both password must be same")
        data.pop('password2')
        return data

        
        