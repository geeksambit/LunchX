from rest_framework import serializers
from quizzes.models import *
from rest_framework import exceptions



class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'
        # read_only_fields = []

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
        # read_only_fields = []
        

class QuizDetailsSerializer(serializers.ModelSerializer):
    
    question = QuestionSerializer(many=True,read_only = True)
    class Meta:
        model = Quiz
        # fields = '__all__'
        fields = ['name', 'active', 'question']