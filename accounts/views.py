from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import RegistrationSerializer , UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate,logout

from .serializers import ProfileSerializers
from .models import Profile
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from rest_framework.authentication import get_authorization_header


class RegistrationView(APIView):
    serializer_class = RegistrationSerializer
    def post(self,request):
        data = request.data
        duplicate_errors = {}

        # Custom duplicate field validation BEFORE serializer.is_valid()
        if User.objects.filter(username=data.get('username')).exists():
            duplicate_errors['username'] = 'Username already exists.'
        if User.objects.filter(email=data.get('email')).exists():
            duplicate_errors['email'] = 'Email already exists.'
        if Profile.objects.filter(phone=data.get('phone')).exists():
            duplicate_errors['phone'] = 'Phone already exists.'
        if Profile.objects.filter(roll=data.get('roll')).exists():
            duplicate_errors['roll'] = 'Roll number already exists.'
        if Profile.objects.filter(registration=data.get('registration')).exists():
            duplicate_errors['registration'] = 'Registration number already exists.'
        if Profile.objects.filter(nationality_number=data.get('nationality_number')).exists():
            duplicate_errors['nationality_number'] = 'Nationality number already exists.'

        if duplicate_errors: 
            return Response({'duplicate_errors': duplicate_errors}, status=status.HTTP_400_BAD_REQUEST)

        form = self.serializer_class(data=request.data)  
        if form.is_valid(): 
            print('inter form ')
            username = form._validated_data['username']
            full_name = form._validated_data['full_name']
            password = form._validated_data['password']
            phone = form._validated_data['phone']
            email = form._validated_data['email']
            roll = form._validated_data['roll']
            registration = form._validated_data['registration']
            session = form._validated_data['session']
            department = form._validated_data['department']
            address = form._validated_data['address']
            blood = form._validated_data['blood']
            gender = form._validated_data['gender']
            birthday = form._validated_data['birthday']
            nationality_type = form._validated_data['nationality_type']
            nationality_number = form._validated_data['nationality_number']
            role = form._validated_data['role']
  
            user =  User.objects.create_user(username=username,password=password,first_name=full_name,email=email)
            user.is_active = False
            user.save()
            profile = Profile.objects.create(user=user,
                                             full_name=full_name,
                                             phone=phone,email=email,
                                             roll=roll,registration=registration,
                                             session=session,department=department,
                                             address=address,blood=blood,
                                             gender=gender,
                                             birthday=birthday,
                                             nationality_type=nationality_type,
                                             nationality_number=nationality_number,
                                             role=role)
            
            from core.emails import Registration_received
            Registration_received(user,profile)
            
            return Response({'success':'Sended Data'},status=status.HTTP_201_CREATED)
        
        return Response("Error",status=status.HTTP_502_BAD_GATEWAY)
    
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            profile = Profile.objects.get(user=user)
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            
            return Response({
                "token_id": token.key,
                "profile_id": profile.id,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                return Response({"error": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

            if profile.role != 'admin':
                return Response({"error": "Only admin users can log in here."}, status=status.HTTP_403_FORBIDDEN)

            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)

            return Response({
                "token_id": token.key,
                "profile_id": profile.id,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request):
        auth_header = get_authorization_header(request).decode('utf-8')

        if not auth_header.startswith('Token '):
            return Response({'error': 'Authorization header must start with Token'}, status=status.HTTP_400_BAD_REQUEST)

        token_key = auth_header.split(' ')[1]

        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            token.delete()
            logout(request)
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

from core.permissions import CustomAdminTokenCheckMixin

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProfileFilter

class ProfileSerializerView(CustomAdminTokenCheckMixin, ModelViewSet):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.filter(user__is_active=True)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfileFilter

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        # Centralized permission check for write operations
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if not self.is_admin(request):
                raise PermissionDenied(detail='Only admins can perform this action.')

    @action(detail=False, methods=['get'], url_path='unactive')
    def get_unactive_profiles(self, request):
        if not self.is_admin(request):
            return Response({'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

        profiles = Profile.objects.filter(user__is_active=False)
        serializer = self.get_serializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='activate')
    def activate_profile(self, request, pk=None):
        if not self.is_admin(request):
            return Response({'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user = profile.user

        from core.emails import Account_verified
        Account_verified(user,profile)
        
        user.is_active = True
        user.save()
        
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    



from django.http import HttpResponse,JsonResponse
from rest_framework import response
import requests

def third_party_api(request):
    context = requests.get('https://alfa-leetcode-api.onrender.com/anmamun0')
    
    return JsonResponse(data=context.json(),safe=False)




# from django.http import HttpResponse,JsonResponse
# from rest_framework import response,status
# from rest_framework.decorators import api_view


# @api_view(['GET'])
# def third_party_api(request):
#     return response.Response('Hello how are you',status=status.HTTP_200_OK)











# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated

# @api_view(['POST'])
# def login_user(request):
#     """
#     Authenticate user and return an authentication token.
#     """
#     username = request.data.get("username")
#     password = request.data.get("password")

#     # Check if username and password are provided
#     if not username or not password:
#         return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         user = User.objects.get(username=username)
#         if not user.check_password(password):
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
#     except User.DoesNotExist:
#         return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#     # Generate or Retrieve Token
#     token, created = Token.objects.get_or_create(user=user)

#     return Response({"token": token.key}, status=status.HTTP_200_OK)
