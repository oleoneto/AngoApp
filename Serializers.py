"""
Serializers.py
Written by Leo Neto
Updated on Aug 25, 2017

Using the django rest framework to query, serialize, and generate views for our models.

"""
from rest_framework.serializers import ModelSerializer
from Website.models import *
from Work.models import *

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'bio', 'photo')
#end PersonSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('uri', 'title', 'client', 'featured',
                  'type', 'artwork', 'description')
#end ProjectSerializer