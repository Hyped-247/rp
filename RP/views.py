from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views.generic.base import View
from Owner.models import Owner
from Renter.models import Renter


class LoginView(View):
    template_name = 'index.html'

    def post(self, request):

        # check if email and password are correct.
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email__iexact=email, password__iexact=password)  # return None if user is not authenticate

        if user is not None:
            login(request, user)  # login the user.

            # if the user is renter, then send him to the renter page.
            if Renter.objects.filter(user=user).exists():
                return redirect('')

            # if the user is owner, then send him to the owner page.
            elif Owner.objects.filter(user=user).exists():
                return redirect('owner:main')
            else:
                # else send him to the owner page.
                return redirect('')

        else:
            raise ValidationError("Invalid email or wrong password")


class LogOut():
    pass
