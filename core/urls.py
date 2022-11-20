
from django.contrib import admin
from django.urls import path

from lead.views import (
    home_page,
lead_detail
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('<pk>/', lead_detail),
]
