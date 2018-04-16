from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from Apt.forms import AptForm
from Apt.models import Apt
from AptBuilding.models import AptBuilding


class AptListView(LoginRequiredMixin, ListView):
    template_name = 'Apt/list.html'

    def get_context_data(self, **kwargs):
        context = super(AptListView, self).get_context_data(**kwargs)
        aptBuilding = AptBuilding.objects.get(id=self.kwargs['pk'])
        context['aptBuilding'] = aptBuilding
        context['Apt'] = Apt.objects.filter(aptBuilding=aptBuilding)
        return context

    def get_queryset(self):
        return User.objects.all()


class DetailApt(LoginRequiredMixin, DetailView):
    template_name = 'Apt/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailApt, self).get_context_data(**kwargs)
        context['Apt'] = Apt.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Apt.objects.all()


class CreateApt(LoginRequiredMixin, CreateView):
    template_name = 'Apt/create.html'
    form_class = AptForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.aptBuilding = AptBuilding.objects.get(id=self.kwargs['pk'])
        post.save()
        return self.get_success_url()

    def get_success_url(self, **kwargs):
        return redirect(reverse('owner:apt:list', kwargs={'pk' : self.kwargs['pk']}))


class UpdateApt(LoginRequiredMixin, UpdateView):
    template_name = 'Apt/update.html'
    model = Apt
    form_class = AptForm
    success_message = "Updated Successfully"

    def get_success_url(self, **kwargs):
        return reverse('owner:apt:list', kwargs={'pk' : self.kwargs['aptBuilding_pk']})


class DeleteApt(LoginRequiredMixin, DeleteView):
    template_name = 'Apt/delete.html'
    model = Apt

    def get_success_url(self, **kwargs):
        return reverse('owner:apt:list', kwargs={'pk' : self.kwargs['aptBuilding_pk']})
