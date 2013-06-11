"""
account.py

Contains view for account management related pages

"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

def process_login(request):
    """
    Authenticates the user (this assumes https is being used such that the
    password does not need to be encrypted by javascript)
    """
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return HttpResponseBadRequest()
    user = authenticate(username=username, password=password)
    signin_page = reverse_lazy("signin")
    home_page = reverse_lazy("home")
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('next', home_page))
        else:
            # inactive account
            return HttpResponseRedirect("%s?e=a"%signin_page)
    else:
        # bad password
        return HttpResponseRedirect("%s?e=p"%signin_page)
        
def process_logout(request):
    """
    logs out the current user
    """
    logout(request)
    return HttpResponseRedirect("/")

def signin_page(request):
    """
    Page to initiate sign-in
    """
    return HttpResponse("TODO: make me")
    
