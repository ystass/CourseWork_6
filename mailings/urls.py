from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingSettingsListView, MailingSettingsDetailView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('mailings/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('mailings/create/', ClientCreateView.as_view(), name='client_create'),
    path('mailings/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('mailings/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('mailings', MailingSettingsListView.as_view(), name='mailingsettings_list'),
    path('mailingsettings/<int:pk>/', MailingSettingsDetailView.as_view(), name='mailingsettings_detail'),
    path('mailingsettings/create/', MailingSettingsCreateView.as_view(), name='mailingsettings_create'),
    path('mailingsettings/<int:pk>/update/', MailingSettingsUpdateView.as_view(), name='mailingsettings_update'),
    path('mailingsettings/<int:pk>/delete/', MailingSettingsDeleteView.as_view(), name='mailingsettings_delete'),
]
