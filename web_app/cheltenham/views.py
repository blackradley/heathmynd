# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.contrib import messages

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    """ index """
    template = get_template('cheltenham/index.html')
    #messages.set_level(request, messages.DEBUG)
    #list(messages.get_messages(request))# clear out the previous messages
    #messages.add_message(request, messages.INFO, 'Hello world.')
    context = {'nbar': 'cheltenham'}
    html = template.render(context, request)
    return HttpResponse(html)
