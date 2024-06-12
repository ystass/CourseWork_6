from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('mailings/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('mailings/create/', ClientCreateView.as_view(), name='client_create'),
    path('mailings/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('mailings/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
