from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from Owner.forms import OwnerForm
from Owner.models import Owner


class RegisterOwner(CreateView):
    template_name = 'Owner/register-owner.html'
    form_class = OwnerForm
    model = Owner

    def form_valid(self, form):
        form.save()
        return redirect('login')


class OwnerMain(ListView):
    template_name = 'Owner/main.html'

"""

<a href="{% url 'register-owner' %}"> Create account for teacher </a><br>


{% include 'register.html' %}
"""