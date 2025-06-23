from django.urls import path , include
from .views import diploma_notices

urlpatterns = [
    path('diploma/',diploma_notices,name='diploma_notices'),
]