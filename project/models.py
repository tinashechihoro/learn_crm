from django.db import models


# Create your models here.
class Project(models.Model):
    PRIVACY_OPTIONS = (
        (
            ('Public', 'Public'),
            ('Private', 'Private'),
            ('Limited', 'Limited'),
        )
    )
    title = models.CharField(
        'Project Title',
        max_length=255
    )
    project_private = models.CharField(
        max_length=50,
        choices=PRIVACY_OPTIONS,
        null=True,
        blank=True
    )
    project_lead = models.CharField(max_length=255,null=True,blank=True)
    start_date = models.DateField(null=True, blank=True)
    deadline_date = models.DateField(null=True, blank=True)
    project_overview = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    budget = models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True)
