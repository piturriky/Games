from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *
from django.contrib.auth.models import User

class GameSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='game-detail',lookup_field='name')
    developers = HyperlinkedRelatedField(many=True, read_only=True,view_name='user-detail',lookup_field='username')
    company = HyperlinkedRelatedField(many=False, read_only=True,view_name='company-detail',lookup_field='name')
    platforms = HyperlinkedRelatedField(many=True, read_only=True,view_name='platform-detail',lookup_field='name')
    class Meta:
        model = Game

class CompanySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='company-detail',lookup_field='name')
    class Meta:
        model = Company

class PlatformSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='platform-detail',lookup_field='name')
    class Meta:
        model = Platform

class DeveloperSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='user-detail',lookup_field='username')
    class Meta:
        model = User
