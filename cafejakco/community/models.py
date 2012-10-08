from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    def __unicode__(self):
        return self.name    

    def save(self, *args, **kwargs):
        return super(Group, self).save(*args, **kwargs)
    
    def serialize(self):
        data = {
                'group_id':self.id,
                'group_name':self.name,
                'created':str(self.created),
                }
        return data

class Article(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    comments = models.PositiveSmallIntegerField(default=0, null=True)
    likes = models.PositiveSmallIntegerField(default=0, null=True)
    image = models.CharField(max_length=80, null=True)
      
    def __unicode__(self):
        return self.title    

    def save(self, *args, **kwargs):
        return super(Article, self).save(*args, **kwargs)
    
    def serialize(self):
        data = {
                'user_id':self.user.id,
                'user_name':self.user.username,
                'group_id':self.group.id,
                'group_name':self.group.name,  
                'article_id':self.id,
                'title':self.title,
                'content':self.content,
                'comments':self.comments,
                'likes':self.likes,
                'image':self.image,
                'created':str(self.created),
                }
        return data

class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(max_length=400, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    article = models.ForeignKey(Article)
    
    def __unicode__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        return super(Comment, self).save(*args, **kwargs)
    
    def serialize(self):
        data = {
                'user_id':self.user.id,
                'user_name':self.user.username,
                'content':self.content,
                'article_id':self.article.id,
                'created':str(self.created),
                }
