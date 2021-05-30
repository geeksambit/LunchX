 
from rest_framework import serializers
from materials.models import *


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = []


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = []