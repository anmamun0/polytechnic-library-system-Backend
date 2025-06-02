from rest_framework.serializers import ModelSerializer, ReadOnlyField , SerializerMethodField
from .models import Transaction 
from datetime import date

class TransactionSerilizers(ModelSerializer):
    # profile = ReadOnlyField(source='profile.user.username')  # Add this field
    book = ReadOnlyField(source='book.isbn')  # Add this field
    warning = SerializerMethodField()
    
    class Meta:
        model = Transaction
        fields = "__all__"  # This includes all fields + the new 'username'
        # Alternatively, you could explicitly list fields like:
        # fields = ['id', 'profile', 'book', 'request_date', 'due_date', 'borrow_date', 'return_date', 'status', 'username']
    def get_warning(self, obj):
        if obj.status not in ['pending', 'borrowed']:
            return None

        if not obj.borrow_date or not obj.return_date:
            return None  # Missing dates, can't calculate

        today = date.today()
        start_date = obj.borrow_date
        end_date = obj.return_date
        due_date = obj.due_date #its int days of for borrowed
        # Days remaining (or overdue if negative)
        delta_days = (end_date - today).days

        return int(delta_days)