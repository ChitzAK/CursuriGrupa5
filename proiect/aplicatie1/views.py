from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from aplicatie1.models import Location


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = ['city', 'country']
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')


class ListLocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['restricted_location'] = Location.objects.filter(company_id=self.request.user.userextend.company.id)
        return data


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_queryset(self):
        if self.request.user.is_superuser is False:
            return self.model.objects.filter(company_id=self.request.user.userextend.company.id)
        return self.model.objects.all()

    def get_success_url(self):
        return reverse('aplicatie1:listare')
