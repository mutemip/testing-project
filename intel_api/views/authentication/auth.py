from intel_api.models import AccessToken
from rest_framework import authentication
from rest_framework import exceptions

class GetRequestAuthenticationBase(authentication.BaseAuthentication):
    
    def authenticate(self,request):
        session_key = request.META.get('HTTP_SESSION_KEY',None) # or request.headers.get('Session-Key')
        header_auth = request.META.get('HTTP_AUTHORIZATION',None)
        if header_auth and session_key:
            token_str, token = header_auth.split()
            if token_str == "Token" and token:
                user = AccessToken.objects.filter(token=token,session_key=session_key).select_related('user_entity').last()
                if user:
                    if not user.is_login:
                        raise exceptions.AuthenticationFailed("User logged out")

                    return user
                else:
                    raise exceptions.AuthenticationFailed("Unable to login.")              
            else:
                raise exceptions.AuthenticationFailed('No authorization token supplied')
        else:
            raise exceptions.AuthenticationFailed('No authorization token or session key supplied')