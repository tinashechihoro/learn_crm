from django.shortcuts import (
render,
get_list_or_404 ,
redirect,
get_object_or_404
)

from .forms import LeadForm
from .models import Lead, Agent


def landing_page(request):
    return render(request,"landing.html")

def home_page(request):
    leads = get_list_or_404(Lead)

    context = {
        'leads': leads

    }
    return render(request, 'lead/home_page.html', context)


def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead

    }
    return render(request, 'lead/lead_detail.html', context)


def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        print('Received a post request')
        form = LeadForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("Lead has been created")
            form.save()
            return redirect('/')


    context = {
        'form': LeadForm
    }
    return render(request, 'lead/lead_create.html', context)


def lead_update(request,pk):
    lead =  get_object_or_404(Lead,pk=pk)
    form =  LeadForm(instance=lead)
    if request.method == "POST":
        form =  LeadForm(request.POST,instance=lead)
        if form.is_valid():
            first_name =  form.cleaned_data['first_name']
            last_name =  form.cleaned_data['last_name']
            age =  form.cleaned_data['age']
            lead.first_name =  first_name
            lead.last_name =  last_name
            lead.age =  age
            lead.save()
            return redirect('/')



    context = {
        'lead': lead,
        'form':form

    }
    return render(request, 'lead/lead_update.html', context)



def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')














