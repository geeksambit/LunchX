


from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from materials import views
from materials.models import *
from materials.serializers import *

# Create your views here.

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def list(self, request):
        queryset = Class.objects.all()
        serializer = ClassSerializer(queryset,many= True)
        # serializer = self.serializer_class
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All class record",
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
                "message" : "Successfully created class record",
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
                "message" : "Successfully updated class record",
            },
            status.HTTP_200_OK
        )



class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request):
        queryset = Subject.objects.all()
        serializer = SubjectSerializer(queryset,many= True)
        # serializer = self.serializer_class
        return Response(
            {
                "data": serializer.data,
                "status" : "ok",
                "code" : 200,
                "message" : "All class record",
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
                "message" : "Successfully created class record",
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
                "message" : "Successfully updated subject record",
            },
            status.HTTP_200_OK
        )
