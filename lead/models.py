from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

class User(AbstractUser):
    pass


class Campaign(TimeStampedModel):
    name =  models.CharField(max_length=255)
    sub_category1 = models.CharField(max_length=255,null=True,blank=True)
    sub_category2 = models.CharField(max_length=255,null=True,blank=True)
    sub_category3 = models.CharField(max_length=255,null=True,blank=True)
    sub_category4 = models.CharField(max_length=255,null=True,blank=True)
    product = models.CharField(max_length=255,null=True,blank=True)

    class Meta:  # new
        verbose_name_plural = "Campaign"

    def __str__(self):
        return self.name


class Agent(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Lead(TimeStampedModel):


    LEAD_STATUS = (
        ('New','New'),
        ('In-progress','In-progress'),
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Sale','Sale'),
        ('Dead-Rejected','Dead-Rejected'),
    )
    PROGRESS_CHOICES = (
        ('awaiting-allocation','awaiting-allocation'),
        ('awaiting-photos','awaiting-photos'),
        ('awaiting-cfa','awaiting-cfa'),
        ('awaiting-ia','awaiting-ia'),
        ('dead-no-contact','dead-no-contact'),
        ('dead-no-interested','dead-no-interested'),
        ('call-back','call-back'),
        ('paper-work-sent','paper-work-sent'),
        ('paper-work-received','paper-work-received'),
        ('pending-triage','pending-triage'),



    )
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    campaign =  models.ForeignKey(Campaign,related_name='lead', on_delete=models.DO_NOTHING)
    case_reference =  models.CharField(max_length=50)
    client_name =  models.CharField(max_length=255)
    status =  models.CharField(max_length=20,default='New',choices=LEAD_STATUS)
    progress =  models.CharField(max_length=50,default='awaiting-allocation',choices=PROGRESS_CHOICES)
    client_phone_number =  models.CharField(max_length=100)
    notes =  models.TextField( null=True, blank=True)
    closers_notes =  models.TextField( null=True, blank=True)

    class Meta:  # new
        verbose_name_plural = "Leads"

    def __str__(self):
        return self.client_name















