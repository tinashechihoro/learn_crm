from django.contrib import admin

from .models import Agent,User,Lead , Campaign



admin.site.site_header = "CRM Lead Manager"
admin.site.site_title = "Lead Manager"
admin.site.index_title = "Lead Manager"

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Campaign)
admin.site.register(Agent)
