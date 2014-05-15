from django.db import models 
class Car(models.Model): 
       name = models.CharField(max_length=150) 
       Company = models.CharField(max_length=150)   
def __unicode__(self): return self.name + " / "+self.Company    