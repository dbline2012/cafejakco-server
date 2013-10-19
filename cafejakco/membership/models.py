from django.db import models
from django.contrib.auth.models import User
from community.models import Group

# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    sex = models.CharField(max_length=10, null=True)
    nickname = models.CharField(max_length=20, null=False)
    point = models.PositiveIntegerField(default=0, null=True)
    image = models.CharField(max_length=80, null=True)
    
    def __unicode__(self):
        return self.user.username    

    def save(self, *args, **kwargs):
        return super(Member, self).save(*args, **kwargs)
    
    def serialize(self):
        data = {
                'user_id':self.user.id,
                'user_name':self.user.username,
                'group_id':self.group.id,
                'group_name':self.group.name,
                'member_id':self.id,
                'sex':self.sex,
                'nickname':self.nickname,
                'point':self.point,
                'image':self.image,
                }
        return data
    
class Coupon(models.Model):
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    end = models.CharField(max_length=20, null=False)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        return super(Coupon, self).save(*args, **kwargs)
    
    def serialize(self):
        data = {
                'coupon_id':self.id,
                'title':self.title,
                'content':self.content,
                'created':str(self.created),
                'end':self.end,
                }
        return data