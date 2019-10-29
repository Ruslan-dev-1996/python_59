from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import CreateView, ListView, UpdateView, DeleteView




class StatusView(ListView):
    template_name = 'status/status_view.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    template_name = 'status/create_status.html'
    model = Status
    fields = ['name']

    def get_success_url(self):
        return reverse('webapp:status_view')

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('webapp:status_view')



class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/delete_status.html'
    context_object_name = 'status'
    error = 'error.html'

    def delete(self, request, *args, **kwargs):
        context = {}
        try:
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.delete()
            return redirect(success_url)
        except ProtectedError as e:
            context['error'] = 'Has error'
            return render(request, 'error.html', context=context)


    def get_success_url(self):
        return reverse('webapp:status_view')