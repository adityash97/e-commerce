from rest_framework import serializers
from .models import UserAuth
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(allow_blank=False,write_only=True)
    password = serializers.CharField(allow_blank=False,write_only=True)
    class Meta:
        model = UserAuth
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'username':{'required':False,'allow_blank':True}
        }
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Both password must be same")
        data.pop('password2')
        return data
    def create(self,validated_data):
        email=validated_data.get('email')
        basename = email.split('@')[0]
        counter = 1
        unique_username = basename
        while UserAuth.objects.filter(username = unique_username).exists():
            unique_username = basename + str(counter)
            counter+=1
        # must use this method to create user as it will call set_password internally which will hash the password else the plain text will be saved as password.
        user = UserAuth.objects.create_user(email=validated_data.get('email'),password=validated_data.get('password'),username=unique_username)
        return user

class UserLoginSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True, write_only=True)
        password = serializers.CharField(required=True, write_only=True)

        
        