from django.shortcuts import render, render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return render_to_response('click/index.html')
