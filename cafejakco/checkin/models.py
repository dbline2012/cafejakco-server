from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Checkin(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    def __unicode__(self):
        return self.user.username    

    def save(self, *args, **kwargs):
        return super(Checkin, self).save(*args, **kwargs)
    
    def serialize(self):
        data = {
                'user_id':self.user.id,
                'user_name':self.user.username,
                'date':str(self.date),
                }
        return data