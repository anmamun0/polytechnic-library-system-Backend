from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate

from .models import Profile

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Profile
        fields = ['username','full_name','password','email','phone','roll','registration','session','address','nationality_type','nationality_number']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True) 

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        print(username,password)
    
        try:
            user =  User.objects.get(username=username) 
        except Exception as e:
            raise serializers.ValidationError("The emal not exist any user")
        
        user = authenticate(username=username,password=password)
        if not user:
            raise serializers.ValidationError('Inalid User')
        if not user.is_active:
            raise serializers.ValidationError('User account is inactive!')
         
        attrs['user'] = user
        return attrs

 
class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = ['id','user','full_name','role','email','phone','roll','registration','session','address','nationality_type','nationality_number']
