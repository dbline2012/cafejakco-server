from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    def __unicode__(self):
        return self.Name    

    def save(self, *args, **kwargs):
        return super(Group, self).save(*args, **kwargs)

class Entry(models.Model):
    User = models.ForeignKey(User)
    Group = models.ForeignKey(Group)
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)
    Comments = models.PositiveSmallIntegerField(default=0, null=True)
    Likes = models.PositiveSmallIntegerField(default=0, null=True)
      
    def __unicode__(self):
        return self.Title    

    def save(self, *args, **kwargs):
        return super(Entry, self).save(*args, **kwargs)

class Comment(models.Model):
    User = models.ForeignKey(User)
    Content = models.TextField(max_length=2000, null=False)
    Created = models.DateTimeField(auto_now_add=True, auto_now=True)
    Entry = models.ForeignKey(Entry)
    
    def __unicode__(self):
        return self.Content
    
    def save(self, *args, **kwargs):
        return super(Comment, self).save(*args, **kwargs)
