from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from project.models import Project


class ProjectCreateView(TemplateView):

    template_name = 'dashboard/project/create-new.html'

