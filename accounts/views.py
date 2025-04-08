from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import RegistrationSerializer , UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate,logout

from .serializers import ProfileSerializers
from .models import Profile

class RegistrationView(APIView):
    serializer_class = RegistrationSerializer
    def post(self,request):
        form = self.serializer_class(data=request.data)
        if form.is_valid():
            username = form._validated_data['username']
            full_name = form._validated_data['full_name']
            password = form._validated_data['password']

            phone = form._validated_data['phone']
            email = form._validated_data['email']
            roll = form._validated_data['roll']
            registration = form._validated_data['registration']
            session = form._validated_data['session']
            address = form._validated_data['address']
            nationality_type = form._validated_data['nationality_type']
            nationality_number = form._validated_data['nationality_number']

            user =  User.objects.create_user(username=username,password=password,first_name=full_name,email=email)
            profile = Profile.objects.create(user=user,full_name=full_name,phone=phone,email=email,roll=roll,registration=registration,session=session,address=address,nationality_type=nationality_type,nationality_number=nationality_number)

            return Response("Sended Data",status=status.HTTP_201_CREATED)
        return Response("Error",status=status.HTTP_502_BAD_GATEWAY)
    
class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            user = serializer._validated_data['user']
            if user:
                token , _ = Token.objects.get_or_create(user=user)
                login(request,user) 

                return Response({"token":token.key,"user_id":user.id, })
            else:
                return Response({"error":"Invalid Credential"})
        return Response(serializer.errors)


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



class ProfileSerializerView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()

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