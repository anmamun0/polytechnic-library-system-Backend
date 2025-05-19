# permissions.py

from rest_framework.authtoken.models import Token
from accounts.models import Profile

class CustomAdminTokenCheckMixin:
    def is_admin(self, request):

        # its best for safe security
        # it will check , Header section has any "Authorization" variable ?
        auth_header = request.headers.get('Authorization')

        # it will check , Body section has any "token_id" variable ?
        token_id = (
            request.data.get('token_id') or
            request.query_params.get('token_id') or
            request.headers.get('token_id')
        )
        if auth_header and auth_header.startswith('Token '):
            token_id = auth_header.split(' ')[1]
  
        if not token_id:
            return False
        try:
            token = Token.objects.get(key=token_id)
            user = token.user
            profile = Profile.objects.get(user=user)
            return profile.role == 'admin'
        except (Token.DoesNotExist, Profile.DoesNotExist):
            return False
