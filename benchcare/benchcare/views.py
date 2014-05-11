import urlparse
from django.conf import settings
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login, logout, authenticate)
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse


def index(request):
    context = RequestContext(request)

    return render_to_response("main/index.html")


def about(request):
    context = RequestContext(request)

    return render_to_response("main/about.html")


def team(request):
    context = RequestContext(request)

    return render_to_response("main/team.html")


def features(request):
    context = RequestContext(request)

    return render_to_response("main/features.html")


def sign_up(request):
    context = RequestContext(request)

    return render_to_response("registration/registration_form.html")


def sign_in(request):
    context = RequestContext(request)

    return render_to_response("registration/login.html")


def pricing_table(request):
    context = RequestContext(request)

    return render_to_response("main/pricing.html")


def how_it_works(request):
    context = RequestContext(request)

    return render_to_response("main/howitworks.html")


def contact_us(request):
    context = RequestContext(request)

    return render_to_response("main/contact.html")
