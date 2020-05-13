from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.




class User_Input(models.Model):

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        )
    
    BOOL_CHOICES = (
        (True, 'Yes'), 
        (False, 'No')
        )

    # user = models.CharField(on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    birth_date = models.DateField(blank=True)
    age = models.IntegerField(blank=False)
    months_as_customer = models.IntegerField(max_length=None, blank=False)
    policy_number = models.IntegerField(max_length=None, blank=False)
    policy_deductable = models.IntegerField(max_length=None, blank=False)
    policy_annual_premium = models.IntegerField(max_length=None, blank=False)
    umbrella_limit = models.IntegerField(max_length=None, blank=False)
    insured_zip = models.IntegerField(max_length=None, blank=False)
    insured_sex = models.CharField(max_length=1, choices=GENDER)
    insured_education_level = models.CharField(max_length=255)
    insured_occupation = models.CharField(max_length=255)
    insured_hobbies = models.CharField(max_length=255)
    insured_relationship = models.CharField(max_length=255)
    capital_gains = models.IntegerField(max_length=None, blank=False)
    capital_loss = models.IntegerField(max_length=None, blank=False)
    incident_type = models.CharField(max_length=255)
    collision_type = models.CharField(max_length=255)
    incident_severity = models.CharField(max_length=255)
    authorities_contacted = models.CharField(max_length=255)
    incident_hour_of_the_day = models.IntegerField(max_length=None, blank=False)
    number_of_vehicles_involved = models.IntegerField(max_length=None, blank=False)
    property_damage = models.BooleanField(choices=BOOL_CHOICES)
    bodily_injuries = models.IntegerField(max_length=None, blank=False)
    witnesses = models.IntegerField(max_length=None, blank=False)
    police_report_available = models.BooleanField(choices=BOOL_CHOICES)
    total_claim_amount = models.IntegerField(max_length=None, blank=False)
    injury_claim = models.IntegerField(max_length=None, blank=False)
    property_claim = models.IntegerField(max_length=None, blank=False)
    vehicle_claim = models.IntegerField(max_length=None, blank=False)
    auto_make = models.CharField(max_length=255)
    auto_year = models.IntegerField(max_length=None, blank=False)

    def __str__(self):
        return "%s"% self.email



    

