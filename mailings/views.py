from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.models import Client, MailingSettings


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mailings:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mailings:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class MailingSettingsListView(ListView):
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    fields = ('start_time', 'end_time', 'periodicity', 'status', 'title', 'text')
    success_url = reverse_lazy('mailings:mailingsettings_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    fields = ('start_time', 'end_time', 'periodicity', 'status', 'title', 'text')
    success_url = reverse_lazy('mailings:mailingsettings_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailingsettings_list')