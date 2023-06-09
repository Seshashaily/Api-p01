from django.db import models

# Create your models here.
class BookMyShow(models.Model):
     Sname=models.CharField(max_length=100)
     Stime=models.TimeField()
     Sdate=models.DateField()
     Slanguages=models.CharField(max_length=100)
     def __str__(self) -> str:
          return self.Sname