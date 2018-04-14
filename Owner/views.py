from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from AptBuilding.models import AptBuilding
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


class ListViewOwner(ListView):
    template_name = 'Owner/main.html'

    def get_context_data(self, **kwargs):
        context = super(ListViewOwner, self).get_context_data(**kwargs)
        context['AptBuilding'] = AptBuilding.objects.filter(owner__user__username__iexact=self.request.user)
        return context

    def get_queryset(self):
        return User.objects.all()

