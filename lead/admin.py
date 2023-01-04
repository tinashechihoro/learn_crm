from django.contrib import admin

from .models import Agent,User,Lead , Campaign



admin.site.site_header = "CRM Lead Manager"
admin.site.site_title = "Lead Manager"
admin.site.index_title = "Lead Manager"

class LeadModelAdmin(admin.ModelAdmin):
    list_display = ('campaign','case_reference','first_name','last_name')
    search_fields  = ('campaign','case_reference','first_name','last_name','date_of_birth')
    



admin.site.register(Lead,LeadModelAdmin)


admin.site.register(Campaign)
admin.site.register(Agent)
