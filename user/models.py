from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()
    
class CustomUser(AbstractUser):
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'
    
    
    EMAIL_TO_USER_TYPE_MAP = {
        'hod': HOD,
        'staff': STAFF,
        'studnet': STUDENT
    }
    
    
    user_type_data = ((HOD, 'HOD'), (STAFF, 'STAFF'), (STUDENT, 'STUDENT'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
