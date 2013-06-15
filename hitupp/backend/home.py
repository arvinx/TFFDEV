"""
home.py

Contains view for a goer's home page

"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

@login_required
def home_page(request):
    """
    View for goer's home page 
    
    TODO: currently not associated with a template - redirects to exp page
    """
    return HttpResponseRedirect("/experience")
    

