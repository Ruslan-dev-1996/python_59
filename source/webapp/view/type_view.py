from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import CreateView,  ListView, UpdateView, DeleteView




class TypeView(ListView):
    template_name = 'type/type_view.html'
    model = Type
    context_key = 'types'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.all()
        return context

class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'type/create_type.html'
    model = Type
    fields = ['type']

    def get_success_url(self):
        return reverse('webapp:type_view')



class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'type/update_type.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_view')



class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'type/delete_type.html'
    context_object_name = 'type'
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
        return reverse('webapp:type_view' )
