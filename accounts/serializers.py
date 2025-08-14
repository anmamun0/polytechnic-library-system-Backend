from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate

from .models import Profile

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = Profile
        fields = ['username','image','full_name','password','email','phone','roll','registration','session','department','address','blood','gender','birthday','nationality_type','nationality_number','role']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()
        password = attrs.get('password', '')

        if not email or not password:
            raise serializers.ValidationError({
                "detail": "Both email and password are required."
            })

        # Check if user exists
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                "detail": "Invalid email or password."
            }) 
        # Check if user is active before password check
        if not user_obj.is_active:
            raise serializers.ValidationError({
                "detail": f"{user_obj.first_name}!  Your account is currently inactive. For assistance, please contact the administrator at anmamun0@gmail.com."
            })
        # Authenticate using username (since Django's default auth uses username)
        user = authenticate(username=user_obj.username, password=password)

        if user is None:
            raise serializers.ValidationError({
                "detail": "Invalid email or password. Please Try again"
            })

        attrs['user'] = user
        return attrs
 
class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    total_book_read = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_total_book_read(self, obj):
        return obj.profile_transactions.filter(status='returned').count()

    def get_rating(self, obj):
        total = self.get_total_book_read(obj)
        return min(5, int((total / 100) * 5))  # ensure max rating is 5
    
    def get_last_login(self,obj):
        return obj.user.last_login if obj.user else None
    def get_is_active(self,obj):
        return obj.user.is_active if obj.user else None