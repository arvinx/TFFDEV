"""
register.py

Contains view for sign-up related views (pages and ajax requests)

"""

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseRedirect
from backend.models import Goer
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError

def signup_page(request):
    """
    Renders the signup page
    """
    return render_to_response('signup.html', {
        # add stuff here
        }, context_instance=RequestContext(request))
        
def process_registration(request):
    """
    Processes registration request. Redirects back to signup page if either
    the email or the username is taken.
    """
    signup_page = reverse_lazy("signup")
    
    try:
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    except KeyError:
        return HttpResponseBadRequest()
        
    # check if e-mail already exists
    if User.objects.filter(email=email).exists():
        return HttpResponseRedirect("%s?e=e"%signup_page)
    
    try:
        user = User(
            first_name = fname,
            last_name = lname,
            username = username,
            email = email,
            is_active = False,
            is_staff = False,
            is_superuser = False,
        )
        user.set_password(password)
        user.save()
    except IntegrityError:
        return HttpResponseRedirect("%s?e=u"%signup_page)
        
    goer = Goer(user=user)
    goer.save()    
    
    # TODO (jsun): show confirmation message"
    return HttpResponse("success!")

    
