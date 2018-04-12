from django.views.generic import CreateView, UpdateView, DeleteView


class CreateAptBuilding(CreateView):
    template_name = 'AptBuilding/create.html'


class UpdateAptBuilding(UpdateView):
    template_name = 'AptBuilding/create.html'


class DeleteAptBuilding(DeleteView):
    template_name = 'AptBuilding/create.html'
