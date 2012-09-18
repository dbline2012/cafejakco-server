from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    def __unicode__(self):
        return self.name    

    def save(self, *args, **kwargs):
        return super(Group, self).save(*args, **kwargs)

class Article(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    comments = models.PositiveSmallIntegerField(default=0, null=True)
    likes = models.PositiveSmallIntegerField(default=0, null=True)
    image = models.CharField(max_length=80, null=False)
      
    def __unicode__(self):
        return self.title    

    def save(self, *args, **kwargs):
        return super(Article, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(max_length=400, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    article = models.ForeignKey(Article)
    
    def __unicode__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        return super(Comment, self).save(*args, **kwargs)
