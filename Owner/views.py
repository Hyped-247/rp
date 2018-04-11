from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from Owner.forms import UserForm
from Owner.models import Owner


class RegisterOwner(CreateView):
    template_name = 'Owner/signup.html'
    form_class = UserForm

    def form_valid(self, form):

        user = form.save()  # This is going to save the user and return it.

        owner = Owner()  # create an owner object, and fill it in with all the needed data.
        owner.user = user
        owner.address_1 = form.cleaned_data['address_1']
        owner.address_2 = form.cleaned_data['address_2']
        owner.city = form.cleaned_data['city']
        owner.state = form.cleaned_data['state']
        owner.zip_code = form.cleaned_data['zip_code']
        owner.save()

        return redirect('login')


class OwnerMain(ListView):
    template_name = 'Owner/main.html'

"""

<a href="{% url 'register-owner' %}"> Create account for teacher </a><br>


{% include 'register.html' %}
"""