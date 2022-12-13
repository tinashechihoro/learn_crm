from django.contrib import admin
from django.urls import path , include

from lead.views import (
    home_page,
    lead_detail,
    lead_create,
    lead_update,
    lead_delete,
    landing_page


)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page,name='landing-page'),
    path('lead/', include('lead.urls')),

]
