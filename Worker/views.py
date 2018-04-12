from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from Worker.forms import UserForm
from Worker.models import Worker


class RegisterWorker(CreateView):
    template_name = 'Worker/signup.html'
    form_class = UserForm

    def form_valid(self, form):
        user = form.save()  # This is going to save the user and return it.
        worker = Worker()  # create an owner object, and fill it in with all the needed data.
        worker.user = user
        worker.skill = form.cleaned_data['skill']
        worker.save()
        return redirect('login')


class ListViewWorker(ListView):
    template_name = 'Worker/main.html'
