from django.contrib import admin
from django.urls import path , include

from lead.views import (
    home_page,

    landing_page


)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page,name='landing-page'),
    path('lead/', include('lead.urls')),

]
