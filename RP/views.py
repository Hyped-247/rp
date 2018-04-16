from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView

from Apt.models import Apt
from AptBuilding.models import AptBuilding
from Owner.models import Owner
from Renter.models import Renter


class Redirect(ListView):

    def render_to_response(self, context, **response_kwargs):

        # if the user is renter, then send him to the renter page.
        if Renter.objects.filter(user=self.request.user).exists():
            return redirect('renter:main')

        # if the user is owner, then send him to the owner page.
        elif Owner.objects.filter(user=self.request.user).exists():
            return redirect('owner:main')
        else:
            # else send him to the worker page.
            return redirect('worker:main')

    def get_queryset(self):
        return User.objects.all()


class Home(ListView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['Apt'] = Apt.objects.all()
        return context

    def get_queryset(self):
        return User.objects.all()