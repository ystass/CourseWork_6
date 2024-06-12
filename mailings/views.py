from django.shortcuts import render
from django.views.generic import ListView

from mailings.models import ServiceClient


class ServiceClientListView(ListView):
    model = ServiceClient
