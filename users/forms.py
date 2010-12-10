from django import forms
from django.utils.translation import ugettext_lazy as _

class RequestAccountForm(forms.Form):
    email_address = forms.EmailField(label=_('Email Address'))
    tos_accept = forms.BooleanField()
