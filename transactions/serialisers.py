from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Transaction

class TransactionSerilizers(ModelSerializer):
    profile = ReadOnlyField(source='profile.user.username')  # Add this field

    class Meta:
        model = Transaction
        fields = "__all__"  # This includes all fields + the new 'username'
        # Alternatively, you could explicitly list fields like:
        # fields = ['id', 'profile', 'book', 'request_date', 'due_date', 'borrow_date', 'return_date', 'status', 'username']
