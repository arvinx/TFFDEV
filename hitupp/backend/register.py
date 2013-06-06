"""
register.py

Contains view for sign-up related views (pages and ajax requests)

"""

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def signup_page(request):
    """
    Renders the signup page
    """
    return render_to_response('signup.html', {
        # add stuff here
        }, context_instance=RequestContext(request))

