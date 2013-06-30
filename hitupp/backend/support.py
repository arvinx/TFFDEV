#!/bin/python
"""
supprot.py

Handles the experience view
"""

from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext

#@login_required
def support(request):
    """
    TODO: the html for this page is currently incomplete
    return HttpResponseRedirect("/experience")
    """
    return render_to_response('support.html', {
        # add stuff here
        }, context_instance=RequestContext(request))
        
