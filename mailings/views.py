from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.models import Client, MailingSettings, Log


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mailings:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class MailingSettingsListView(ListView):
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    fields = ('client', 'start_time', 'end_time', 'periodicity', 'status', 'title', 'text')
    success_url = reverse_lazy('mailings:mailingsettings_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    fields = ('start_time', 'end_time', 'periodicity', 'status', 'title', 'text')
    success_url = reverse_lazy('mailings:mailingsettings_list')


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailingsettings_list')


class LogListView(ListView):
    model = Log
