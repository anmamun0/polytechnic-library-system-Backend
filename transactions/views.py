from django.shortcuts import render
from .models import Transaction
from .serialisers import TransactionSerilizers
from rest_framework.viewsets import ModelViewSet

from core.permissions import CustomAdminTokenCheckMixin
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
# Create your views here.
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta
from accounts.models import Profile



from django_filters.rest_framework import DjangoFilterBackend 
from .filters import TransactionFilter

class TransactionView(CustomAdminTokenCheckMixin,ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerilizers
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def list(self,request,*args,**kwargs):
        if self.is_admin(request):
            return super().list(request,*args,**kwargs)
        else:
            auth_header = request.headers.get('Authorization')
            token_id = None
            if auth_header and auth_header.startswith('Token '):
                token_id = auth_header.split(' ')[1]
            if not token_id:
                return Response({'detail': 'Requirtment the Token in Head'}, status=status.HTTP_403_FORBIDDEN)
            try:
                token = Token.objects.get(key=token_id)
                user = token.user 
                profile = Profile.objects.get(user=user)
                queryset = Transaction.objects.filter(profile=profile)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
        
            except Exception as e:
              return Response({'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
            
    def create(self, request, *args, **kwargs): 
        auth_header = request.headers.get('Authorization')
        token_id = None
        if auth_header and auth_header.startswith('Token '):
            token_id = auth_header.split(' ')[1]
        
        if not token_id:
            return Response({'detail': 'Token is not provided or invalid'}, status=status.HTTP_403_FORBIDDEN)

        try:
            token = Token.objects.get(key=token_id)
            user = token.user
            profile = Profile.objects.get(user=user)
            
        except Token.DoesNotExist:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)

        book_id = request.data.get('book')
        due_date = request.data.get('due_date') 

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        # Check for existing transaction (pending or borrowed)

        existing_transaction = Transaction.objects.filter(profile=profile,book=book,
        status__in=["pending", "borrowed"]).first()

        if existing_transaction:
            if existing_transaction.status == "pending":
                return Response({"error": "You already have a pending request for this book."},status=400)
            elif existing_transaction.status == "borrowed":
                return Response(
                    {"error": "You are currently borrowing this book. Please return it before requesting again."},status=400)

        if not book_id or not due_date:
            return Response({'detail': 'book and due_date are required'}, status=status.HTTP_400_BAD_REQUEST)
 
       

        transaction = Transaction.objects.create(profile=profile, book=book, due_date=due_date)
 
        serializer = self.get_serializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def partial_update(self, request, *args, **kwargs):
        # Step 1: Check admin access
        if not self.is_admin(request):
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        # Step 2: Get transaction
        instance = self.get_object()

        # Step 3: Get status from request
        new_status = request.data.get('status')
        if not new_status:
            return Response({'detail': 'Status is required.'}, status=status.HTTP_400_BAD_REQUEST)

        book = instance.book

        # Step 4: Handle borrow
        if new_status == 'borrowed':
            if book.available <= 0:
                return Response({'detail': 'Book is currently unavailable.'}, status=status.HTTP_400_BAD_REQUEST)

            instance.status = 'borrowed'
            instance.borrow_date = timezone.now()

            # Handle due date
            try:
                days_due = int(instance.due_date)
            except (ValueError, TypeError):
                days_due = 7  # default fallback

            instance.return_date = instance.borrow_date.date() + timedelta(days=days_due)
            instance.save()

            book.available -= 1
            book.save()

        # Step 5: Handle return
        elif new_status == 'returned':
            if instance.status != 'borrowed':
                return Response({'detail': 'This book is not currently borrowed.'}, status=status.HTTP_400_BAD_REQUEST)

            instance.status = 'returned' 
            instance.save()

            book.available += 1
            book.save()

        else:
            return Response({'detail': 'Invalid status. Must be "borrowed" or "returned".'}, status=status.HTTP_400_BAD_REQUEST)

        # Step 6: Respond
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
          # Only check admin for write operations (POST, PATCH)
        if request.method in ['PUT','DELETE']:
            if not self.is_admin(request):
                raise PermissionDenied(detail='Only admins can perform this action.')

