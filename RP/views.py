from django.shortcuts import redirect
from django.views.generic import FormView
from Owner.models import Owner
from RP.forms import Login
from Renter.models import Renter


class LoginIn(FormView):
    template_name = 'index.html'
    form_class = Login

    def form_valid(self, form):
        if form.is_valid():  # check if email and password are correct.

            # if the user is renter, then send him to the renter page.
            if Renter.objects.filter(user__username__iexact=self.request.user).exists():
                return redirect('')

            # if the user is owner, then send him to the owner page.
            elif Owner.objects.filter(user__username__iexact=self.request.user).exists():
                return redirect('owner:main')
            else:
                # else send him to the owner page.
                return redirect('')


class LogOut():
    pass
