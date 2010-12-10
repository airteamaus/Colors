from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext

from users.forms import RequestAccountForm

def request_account(request, next='/', template='users/request_account.html'):
    """
    Request the users email address then send them an email with a confirmation link
    """
    context_dict = {
        'form': RequestAccountForm(),
        'next': next,
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))

def request_account_confirm(request, template='users/request_account_confirm.html'):
    """
    Receive that confirmation link, redirect to set_password()
    """
    context_dict = {
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))

def set_password(request, template='users/set_password.html'):
    """
    Set, or Reset, the users password
    """
    context_dict = {
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))
    
def login(request, template='users/login.html'):
    """
    Log the user in
    """
    context_dict = {
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))