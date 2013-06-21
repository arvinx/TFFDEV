#!/bin/python
"""
storyboard.py

Handles the storyboard view
"""

from django.shortcuts import render_to_response
from django.template import RequestContext

def storyboard(request):
    """
    TODO: storyboard is likely just a sub-page
    """
    return render_to_response('storyboard.html', {
        # add stuff here
        }, context_instance=RequestContext(request))
        
