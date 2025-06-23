from rest_framework.viewsets import ModelViewSet
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from accounts.models import Profile  # adjust if your Profile model is elsewhere 
from core.permissions import CustomAdminTokenCheckMixin

from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter


class BookViewSet(CustomAdminTokenCheckMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs) 
        # Only check admin for write operations (POST, PATCH)
        if request.method in ['POST', 'PATCH','PUT','DELETE']:
            if not self.is_admin(request):
                raise PermissionDenied(detail='Only admins can perform this action.')


class CategoryViewSet(CustomAdminTokenCheckMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs) 
        # Only check admin for write operations (POST, PATCH)
        if request.method in ['POST', 'PATCH','PUT','DELETE']:
            if not self.is_admin(request):
                raise PermissionDenied(detail='Only admins can perform this action.')
            

            
# single single all request check 
# class BookViewSet(CustomAdminTokenCheckMixin, ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def create(self, request, *args, **kwargs):
#         if not self.is_admin(request):
#             return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
#         return super().create(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         if not self.is_admin(request):
#             return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
#         return super().update(request, *args, **kwargs)
    
#     def partial_update(self, request, *args, **kwargs):
#         if not self.is_admin(request):
#             return Response({'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
#         return super().partial_update(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         if not self.is_admin(request):
#             return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
#         return super().destroy(request, *args, **kwargs)

