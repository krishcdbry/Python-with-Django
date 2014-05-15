from django.db import models

class Cdbry(models.Model):
    name = models.CharField(max_length=150)
    relation=models.CharField(max_length=150)
def __unicode__(self):
    return self.name+"/"+self.relation
 
