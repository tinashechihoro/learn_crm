from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import LeadForm
from .models import Lead, Agent


def landing_page(request):
    return render(request, "landing.html")


class LeadListView(ListView):
    model = Lead
    template_name = "lead/home_page.html"
    context_object_name = "leads"


def home_page(request):
    leads = get_list_or_404(Lead)

    context = {"leads": leads}
    return render(request, "lead/home_page.html", context)


class LeadDetailView(DetailView):
    model = Lead
    template_name = "lead/lead_detail.html"


class LeadCreateView(CreateView):
    model = Lead
    template_name = "lead/lead_create.html"
    fields = [
        "campaign",
        "title",
        "first_name",
        "last_name",
        "national_insuarance",
        "mobile_number",
        "work_number",
        "home_number",
        "address",
        "postal_code",
        "status",
    ]


class LeadUpdateView(UpdateView):
    model = Lead
    template_name = "lead/lead_update.html"


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
