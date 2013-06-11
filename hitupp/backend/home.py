"""
home.py

Contains view for a goer's home page

"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse_lazy

@login_required
def home_page(request):
    """
    View for goer's home page 
    
    TODO: currently not associated with a template
    """
    return HttpResponse("Hi %s (%s)"%(
        request.user.get_full_name(), 
        request.user.username)
    )
    

