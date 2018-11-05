# -*- coding: utf-8 -*-
""" test """
from __future__ import unicode_literals
from django.template.loader import get_template

# Create your views here.
from django.http import HttpResponse

def index(request):
    """ index """
    template = get_template('cornwall/index.html')
    html = template.render()
    return HttpResponse(html)
