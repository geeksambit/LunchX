from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from quizzes.models import *
from quizzes.serializers import *

# Create your views here.

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def list(self, request):
        queryset = Quiz.objects.all()
        serializer = QuizSerializer(queryset,many= True)
        # serializer = self.serializer_class
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All quiz record",
            },
            status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk=None):
            queryset = Quiz.objects.all()
            quiz = get_object_or_404(queryset, pk=pk)
            serializer = QuizSerializer(quiz)
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Got single question record",
            },
            status.HTTP_200_OK
        )


    def create(self, request):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data, context={'request' : request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully created quiz record",
            },
            status.HTTP_200_OK
        )

    def update(self, request, pk=None):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        data.save()

        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully updated quiz record",
            },
            status.HTTP_200_OK
        )


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset,many= True)
        # serializer = self.serializer_class
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All question record",
            },
            status.HTTP_200_OK
        )
    def retrieve(self, request, pk=None):
            queryset = Question.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = QuestionSerializer(user)
            return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Got single question record",
            },
            status.HTTP_200_OK
        )


    def create(self, request):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data, context={'request' : request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully created question record",
            },
            status.HTTP_200_OK
        )

    def update(self, request, pk=None):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        data.save()

        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "Successfully updated question record",
            },
            status.HTTP_200_OK
        )
    
class QuizDetailViewSet(APIView):
  
    def get(self, request):
            queryset = Quiz.objects.all()
            serializer = QuizDetailsSerializer(queryset,many= True)
            # serializer = self.serializer_class
            return Response(
                {
                    "data": serializer.data,
                    "status" : "ok",
                    "code" : 200,
                    "message" : "All quiz detail record",
                },
                status.HTTP_200_OK
            )

