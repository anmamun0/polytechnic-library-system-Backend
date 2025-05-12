from django.urls import path,include

from .views import InactiveStudentListView, ActiveStudentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pending_student', InactiveStudentListView, basename='pending-student')
router.register('active_student', ActiveStudentListView, basename='active-student')

urlpatterns = [
    path('', include(router.urls)),  # No slash here
]