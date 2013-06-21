#!/bin/python
"""
experience.py

Handles the experience view
"""

from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required

def experience(request):
    """
    TODO: the html for this page is currently incomplete
    """
    return render_to_response('experience.html', {
        # add stuff here
        }, context_instance=RequestContext(request))
        
