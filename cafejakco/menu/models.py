from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=80, null=False, unique=True)
    category = models.CharField(max_length=20, null=False)
    desc = models.TextField(null=False)
    cost = models.PositiveSmallIntegerField(default=0, null=True)
    def __unicode__(self):
        return self.name    

    def save(self, *args, **kwargs):
        return super(Menu, self).save(*args, **kwargs)

    def serialize(self):
        data = {'name':self.name,
                'category':self.category,
                'desc':self.desc,
                'cost':self.cost,
               } 
	return data
