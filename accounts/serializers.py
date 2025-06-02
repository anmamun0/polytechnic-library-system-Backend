from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate

from .models import Profile

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = Profile
        fields = ['username','full_name','password','email','phone','roll','registration','session','department','address','blood','nationality_type','nationality_number','role']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')  
        print(email,' - ' , password)
        # Check if user with this email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("No user is registered with this email.")
        
        user = authenticate(username=user.username, password=password)
        print(user.username)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is inactive.")

        attrs['user'] = user
        return attrs
 
class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    total_book_read = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_total_book_read(self, obj):
        return obj.profile_transactions.filter(status='returned').count()

    def get_rating(self, obj):
        total = self.get_total_book_read(obj)
        return min(5, int((total / 100) * 5))  # ensure max rating is 5
