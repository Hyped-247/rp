from django.shortcuts import redirect
from django.views.generic import CreateView
from Owner.forms import OwnerForm
from Owner.models import Owner


class RegisterOwner(CreateView):
    template_name = 'Owner/renter.html'
    form_class = OwnerForm
    model = Owner

    def form_valid(self, form):
        form.save()
        return redirect('login')
