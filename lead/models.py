from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Campaign(TimeStampedModel):
    name = models.CharField(max_length=255)
    sub_category1 = models.CharField(max_length=255, null=True, blank=True)
    sub_category2 = models.CharField(max_length=255, null=True, blank=True)
    sub_category3 = models.CharField(max_length=255, null=True, blank=True)
    sub_category4 = models.CharField(max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)

    class Meta:  # new
        verbose_name_plural = "Campaign"

    def __str__(self):
        return self.name


class Agent(models.Model):
    user = models.OneToOneField(User, default=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Lead(TimeStampedModel):
    TITLES_CHOICES = (
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
        ("Miss", "Miss"),
        ("Ms", "Ms"),
    )

    LEAD_STATUS = (
        ("New", "New"),
        ("In-progress", "In-progress"),
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Sale", "Sale"),
        ("Dead-Rejected", "Dead-Rejected"),
    )
    PROGRESS_CHOICES = (
        ("awaiting-allocation", "awaiting-allocation"),
        ("awaiting-photos", "awaiting-photos"),
        ("awaiting-cfa", "awaiting-cfa"),
        ("awaiting-ia", "awaiting-ia"),
        ("dead-no-contact", "dead-no-contact"),
        ("dead-no-interested", "dead-no-interested"),
        ("call-back", "call-back"),
        ("paper-work-sent", "paper-work-sent"),
        ("paper-work-received", "paper-work-received"),
        ("pending-triage", "pending-triage"),
    )
    agent = models.ForeignKey(
        get_user_model(), default=get_user_model(), on_delete=models.CASCADE
    )
    campaign = models.ForeignKey(
        Campaign, related_name="lead", on_delete=models.DO_NOTHING
    )
    case_reference = AutoSlugField(populate_from="id", unique=True)
    title = models.CharField(
        max_length=10, choices=TITLES_CHOICES, null=True, blank=True
    )
    entry_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_insurance = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=50, null=True, blank=True)
    work_number = models.CharField(max_length=50, null=True, blank=True)
    home_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, default="New", choices=LEAD_STATUS)
    progress = models.CharField(
        max_length=50, default="awaiting-allocation", choices=PROGRESS_CHOICES
    )
    notes = models.TextField(null=True, blank=True)
    closers_notes = models.TextField(null=True, blank=True, )
    inspection_auditor_file = models.FileField(upload_to="media", null=True, blank=True)

    class Meta:  # new
        verbose_name_plural = "Leads"

    def __str__(self):
        return self.first_name
