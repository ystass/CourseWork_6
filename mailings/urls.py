from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import ServiceClientListView

app_name = MailingsConfig.name

urlpatterns = [
    path('', ServiceClientListView.as_view(), name='mailings_list'),
]
