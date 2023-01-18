
from django.urls import path

from project.views import ProjectCreateView

urlpatterns = [
    path("", ProjectCreateView.as_view(),name='project-create'),

]

