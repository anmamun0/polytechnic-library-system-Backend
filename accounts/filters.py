# filters.py
import django_filters
from .models import Profile

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'full_name': ['icontains', 'exact'],
            'role': ['exact'],
            'phone': ['icontains', 'exact'],
            'email': ['icontains', 'exact'],
            'roll': ['icontains', 'exact'],
            'registration': ['icontains', 'exact'],
            'department': ['exact', 'icontains'],
            'session': ['exact'],
            'address': ['icontains'],
            'blood': ['exact'],
            'nationality_type': ['exact'],
            'nationality_number': ['icontains', 'exact'],
            'user__is_active': ['exact'],  # optional, if you want to filter active/inactive users
        }
