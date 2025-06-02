import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    isbn = django_filters.CharFilter(field_name='isbn', lookup_expr='exact')
    language = django_filters.CharFilter(field_name='language', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    
    min_copies = django_filters.NumberFilter(field_name='copies', lookup_expr='gte')
    max_copies = django_filters.NumberFilter(field_name='copies', lookup_expr='lte')
    min_available = django_filters.NumberFilter(field_name='available', lookup_expr='gte')
    max_available = django_filters.NumberFilter(field_name='available', lookup_expr='lte')

    class Meta:
        model = Book
        fields = []  # leave empty since we’re declaring filters explicitly
