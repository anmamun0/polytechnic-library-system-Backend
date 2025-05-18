from django.urls import path,include

from .views import PendingStudentListView, ActiveStudentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pending_student', PendingStudentListView, basename='pending_student')
router.register('active_student', ActiveStudentListView, basename='active_student')

urlpatterns = [
    path('', include(router.urls)),
]