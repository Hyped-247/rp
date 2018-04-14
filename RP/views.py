from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView
from Owner.models import Owner
from Renter.models import Renter


class Redirect(ListView):

    def render_to_response(self, context, **response_kwargs):

        # todo: find a way to run quires using filter.
        Renter.objects.filter(user__username__iexact=self.request.user).exists()

        # if the user is renter, then send him to the renter page.
        if Renter.objects.filter(user__username__iexact=self.request.user).exists():
            return redirect('renter:main')

        # if the user is owner, then send him to the owner page.
        elif Owner.objects.filter(user__username__iexact=self.request.user).exists():
            return redirect('owner:main')
        else:
            # else send him to the worker page.
            return redirect('worker:main')

    def get_queryset(self):
        return User.objects.all()
