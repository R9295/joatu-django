import re

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

from django.utils.deprecation import MiddlewareMixin



EXEMPT_URLS= [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        #if not request.user.is_authenticated:
        #    if not any(url.match(path) for url in EXEMPT_URLS):
        #        return redirect(settings.LOGIN_URL)

        url_is_exempt= any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('accounts:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            if not user.profile:
                return redirect('profiles:create')
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated or url_is_exempt:
            return None

        else:
            return redirect(settings.LOGIN_URL)

class ProfileRequiredMiddleware(MiddlewareMixin):


    def process_request(self, request):
        if request.path == '/rest-auth/logout/':
            return None
        if request.user.is_authenticated:
            if not request.user.profileIsCreated:
                if request.path == '/profiles/create/' or request.path =='/api/profiles/create/':
                    return None
                else:
                    return redirect('/profiles/create')
            else:
                return None
        else:
            return None
    #def process_request( self, request ):
    #    print( "func" )
    #    print(request.user.profileIsCreated)

    #    if request.user.is_authenticated and not request.user.profileIsCreated:
    #        return redirect('/profiles/create/')
    #    else:
    #        return None
