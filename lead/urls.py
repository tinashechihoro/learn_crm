from django.contrib import admin
from django.urls import path

from lead.views import (
    LeadListView,
    LeadDetailView,
    LeadUpdateView,
    LeadDeleteView,
    LeadCreateView,
    home_page,

    landing_page

)

urlpatterns = [

    path('landing/', home_page, name='landing-page'),
    path('', LeadListView.as_view(), name='lead-list'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),

    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
]
