from django.shortcuts import redirect
from django.views.generic import CreateView
from Renter.forms import UserForm
from Renter.models import Renter


class RegisterRenter(CreateView):
    template_name = 'Renter/signup.html'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save()  # This is going to save the user and return it.

        renter = Renter()  # create an owner object, and fill it in with all the needed data.
        renter.user = user
        renter.has_animal = form.cleaned_data['has_animal']
        renter.is_smoker = form.cleaned_data['is_smoker']
        renter.is_single = form.cleaned_data['is_single']
        renter.job = form.cleaned_data['job']
        renter.save()
        return redirect('login')
