import django_filters
from accounts.models import Profile

class StudentFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(field_name='role',lookup_expr='exact')
    phone = django_filters.CharFilter(field_name='phone',lookup_expr='exact')
    email = django_filters.CharFilter(field_name='email',lookup_expr='exact')
    registration = django_filters.CharFilter(field_name='registration',lookup_expr='exact')
    department = django_filters.CharFilter(field_name='department',lookup_expr='exact')
    session = django_filters.CharFilter(field_name='session',lookup_expr='exact')
    nationality_type = django_filters.CharFilter(field_name='nationality_type',lookup_expr='exact')
    nationality_number = django_filters.CharFilter(field_name='nationality_number',lookup_expr='exact')
    class Meta:
        model = Profile
        fields = ['role','phone','email','registration','department','session','nationality_type','nationality_number']

