from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from AptBuilding.forms import AptBuildingForm
from AptBuilding.models import AptBuilding
from Owner.models import Owner


class CreateAptBuilding(LoginRequiredMixin, CreateView):
    template_name = 'AptBuilding/create.html'
    form_class = AptBuildingForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = Owner.objects.get(user=self.request.user)
        post.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect(reverse('owner:main'))


class DetailAptBuilding(LoginRequiredMixin, DetailView):
    template_name = 'AptBuilding/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailAptBuilding, self).get_context_data(**kwargs)
        context['AptBuilding'] = AptBuilding.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return AptBuilding.objects.all()


class UpdateAptBuilding(LoginRequiredMixin, UpdateView):
    template_name = 'AptBuilding/update.html'
    model = AptBuilding
    form_class = AptBuildingForm
    success_message = "Updated Successfully"

    def get_success_url(self):
        return reverse('owner:main')


class DeleteAptBuilding(LoginRequiredMixin, DeleteView):
    template_name = 'AptBuilding/delete.html'
    model = AptBuilding

    def get_success_url(self):
        return reverse('owner:main')
