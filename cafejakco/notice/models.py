from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    image = models.CharField(max_length=80, null=True)
    
    def __unicode__(self):
        return self.name    

    def save(self, *args, **kwargs):
        return super(Notice, self).save(*args, **kwargs)
    
    def serialize(self):
	data = {'title':self.title,
		#'content':self.content,
		}
	return data
