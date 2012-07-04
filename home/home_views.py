# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 04/02/12
#Ultima alteracao:

from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):


    return render_to_response("home/home.html", RequestContext(request, {} ))