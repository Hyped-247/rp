from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from AptBuilding.forms import AptBuildingForm
from AptBuilding.models import AptBuilding
from Owner.models import Owner


class CreateAptBuilding(LoginRequiredMixin, CreateView):
    template_name = 'AptBuilding/create.html'
    form_class = AptBuildingForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = Owner.objects.get(user__username__iexact=self.request.user)
        post.save()
        return self.get_success_url()

    def get_success_url(self):
        return HttpResponseRedirect('owner:main')


class UpdateAptBuilding(LoginRequiredMixin, UpdateView):
    template_name = 'AptBuilding/update.html'
    model = AptBuilding
    form_class = AptBuildingForm
    success_message = "Updated Successfully"

    def get_success_url(self):
        return redirect('owner:main')


class DeleteAptBuilding(LoginRequiredMixin, DeleteView):
    template_name = 'AptBuilding/delete.html'
    model = AptBuilding

    def get_success_url(self):
        return redirect('owner:main')
