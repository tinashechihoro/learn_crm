from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lead.views import home_page, landing_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing_page, name="landing-page"),
    path("lead/", include("lead.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("project/", include("project.urls")),
    path("lead/", include("lead.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
