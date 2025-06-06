from django.urls import path,include
from .views import RegistrationView ,UserLoginView,UserLogoutView,AdminLoginView

from rest_framework.routers import DefaultRouter
from .views import ProfileSerializerView , third_party_api

router = DefaultRouter()
router.register('',ProfileSerializerView,basename='profile')

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register'), 
    path('login/',UserLoginView.as_view(),name='login'), 
    path('admin_login/',AdminLoginView.as_view(),name='admin_login'), 
    path('logout/',UserLogoutView.as_view(),name='logout'), 
    path('profile/',include(router.urls)),
    
    path('leetcode/',third_party_api,name='leetcode'), 
]