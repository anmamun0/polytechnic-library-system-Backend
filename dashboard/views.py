from django.shortcuts import render
# Create your views here.
from .serializers import NewRegisterSerializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from accounts.models import Profile
from rest_framework_simplejwt.tokens import AccessToken  # JWT decoding
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from django_filters import rest_framework
from .filter import StudentFilter

class PendingStudentListView(ModelViewSet): 
    queryset = Profile.objects.filter(user__is_active=False)
    serializer_class = NewRegisterSerializers
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = StudentFilter

    @extend_schema(
        methods=["PUT"],
        parameters=[
            OpenApiParameter(name='pk', description='Profile ID', required=True, type=int, location=OpenApiParameter.PATH),
        ],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "token_id": {"type": "string", "description": "Admin's auth token"}
                },
                "required": ["token_id"]
            }
        },
        responses={200: OpenApiExample("User Activated", value={"message": "User activated successfully"})}
    )

    @action(detail=True, methods=['put'], url_path='activate')
    def activate_user(self, request, pk=None):
        token_id = request.data.get('token_id')
        if not token_id:
            return Response({'error': 'token_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(key=token_id)
            user = token.user
            admin_profile = Profile.objects.get(user=user)
             
            if admin_profile.role != 'admin':
                return Response({'error': 'Only admin can activate users'}, status=status.HTTP_403_FORBIDDEN)

            # Activate the user (target profile)
            profile = self.get_object()
            profile.user.is_active = True
            profile.user.save()
            
            from core.emails import Account_verified
            Account_verified(user,profile)

            return Response({'message': 'User activated successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['post'], url_path='delete')
    def delete_user(self, request, pk=None):
        token_id = request.data.get('token_id')
        if not token_id:
            return Response({'error': 'token_id is required!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(key=token_id)
            user = token.user
            admin_profile = Profile.objects.get(user=user)
            if admin_profile.role != 'admin':
                return Response({'error': 'Only admin can delete users'}, status=status.HTTP_403_FORBIDDEN)
            
            profile = self.get_object()
            profile.user.delete()  # Also delete the User object
            profile.delete()

            return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class ActiveStudentListView(ModelViewSet):
    queryset = Profile.objects.filter(user__is_active=True)
    serializer_class = NewRegisterSerializers

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = StudentFilter
     