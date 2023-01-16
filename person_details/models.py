from django.db import models

class NextOfKeen(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    address = models.TextField()
    home_number = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=255, null=True, blank=True)




class PersonalIdentifiableInformation(models.Model):

    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    middle_name =  models.CharField(max_length=255,null=True,blank=True)
    national_identity_number = models.CharField(max_length=50)
    gender =  models.CharField(max_length=10,choices=GENDER_CHOICES)
    date_of_birth  =  models.DateField()
    address =  models.TextField()
    home_number =  models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    email =  models.EmailField(null=True,blank=True)











