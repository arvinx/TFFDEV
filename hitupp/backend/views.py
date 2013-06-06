"""
views.py

Contains view for front page and FAQ page

"""

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import django_mobile

def front_page(request):
    """
    Renders the front page
    """
    return render_to_response('index.html', {
        # add stuff here
        }, context_instance=RequestContext(request))
