from django.contrib import admin
from django.urls import path

from lead.views import (
    home_page,
    lead_detail,
    lead_create,
    lead_update,
    lead_delete,
    landing_page


)

urlpatterns = [

    path('landing/', landing_page,name='landing-page'),
    path('', home_page,name='lead-list'),
    path('create/', lead_create,name='lead-create'),

    path('<int:pk>/update/', lead_update,name='lead-update'),
    path('<int:pk>/delete/', lead_delete,name='lead-delete'),
    path('<int:pk>/', lead_detail,name='lead-detail'),
]
