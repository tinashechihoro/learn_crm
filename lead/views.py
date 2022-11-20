from django.shortcuts import render ,get_list_or_404

from .models import Lead,Agent,User
def home_page(request):
    leads  =  get_list_or_404(Lead)

    context = {
        'leads':leads

    }
    return render(request,'lead/home_page.html',context)

def lead_detail(request,pk):
    print(pk)
    lead =  Lead.objects.get(id=pk)
    context = {
        'lead': lead

    }
    return render(request, 'lead/lead_detail.html', context)

def lead_create(request):
    context = {

    }
    return render(request, 'lead/lead_detail.html', context)



