from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class validate(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id=models.BigAutoField;
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    # email=models.EmailField(max_length=122)
    # subject=models.CharField(max_length=180)
    # message=models.TextField()
    # date=models.DateField()
    def __str__(self) :
        return self.username