from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, TemplateView
from RP.forms import Login


class LoginIn(FormView):
    template_name = 'index.html'
    form_class = Login

    def form_valid(self, form):
        if form.is_valid():
            pass
        else:
            return HttpResponseRedirect(self.request.path_info)


