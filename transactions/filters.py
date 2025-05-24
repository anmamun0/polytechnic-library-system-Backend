import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    # Example filters:
    profile = django_filters.CharFilter(field_name='profile', lookup_expr='icontains')
    book__title = django_filters.CharFilter(field_name='book__title', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    due_date = django_filters.NumberFilter(field_name='due_date', lookup_expr='exact')
    request_date = django_filters.DateFromToRangeFilter(field_name='request_date')
    borrow_date = django_filters.DateFromToRangeFilter(field_name='borrow_date')
    return_date = django_filters.DateFromToRangeFilter(field_name='return_date')

    class Meta:
        model = Transaction
        fields = ['profile', 'book__title', 'status','due_date','request_date','borrow_date','return_date']
