from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse


def index(request):
	return HttpResponse("Benchcare about us page")
	
	
