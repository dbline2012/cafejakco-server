from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from django.contrib.auth.models import User
from community.models import *


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        excludes = ['Group']
        fields = ['user', 'title', 'content', 'created', 'comments']
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        #filtering = {
        #    'User': ALL_WITH_RELATIONS,
        #    'Created': ['exact', 'lt', 'lte', 'gte', 'gt'],
        #}
        
#class CommentResource(ModelResource):
#    user = fields.ForeignKey(UserResource, 'user')
#    article = fields.ForeignKey(EntryResource, 'article')
#    
#    class Meta:
#        queryset = Comment.obejcts.filter(article=)