from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from Owner.models import Owner
from Renter.models import Renter

"""
class Login(LoginView):
    template_name = 'registration/login.html'

    def get_redirect_url(self):
        pass

    def post(self, request, *args, **kwargs):

        # check if email and password are correct.
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = authenticate(email=email, password=password)  # return None if user is not authenticate
        print(user)

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


class Logout(LogoutView):
    next_page = 'login.html'
"""
