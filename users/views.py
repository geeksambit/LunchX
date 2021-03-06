from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from users.serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    # permission_classes = [IsAuthenticated|ReadOnly]
    # serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return UserUpdateSerializer
        return UserRegistrationSerializer
    
    def get_object(self):
        return self.request.user
    
    def create(self, request):
        print(request.data)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data =  serializer.data
            data.update({
                "status" : "Active",
            })
            return Response(
                {
                        "data": { "user" : data },
                        "status" : "ok",
                        "code" : 200,
                        "message" : "Thank you for creating your account with LunchX.",
                        "errors" : []
                },
                status.HTTP_200_OK
            )
            # return Response(serializer.validated_data, status=status.HTTP_200_OK)
        res = {
            'message' : serializer.errors['email'],
            'status' : "Bad Request",
            'code' : status.HTTP_400_BAD_REQUEST,
            'errors' : []
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

class MyTokenObtainPairView(TokenObtainPairView):     
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        if  'auth_provider'  in request.POST :
            auth_provider = request.data['auth_provider']

            #social log in 
            if auth_provider == 'google':
                google_serializer_class = GoogleSocialAuthSerializer
                serializer = google_serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                data = ((serializer.validated_data)['auth_token'])
                return Response(
                    {
                            "data": { "user" : data },
                            "status" : "ok",
                            "code" : 200,
                            "message" : "Thank you for creating your LunchX account.",
                            "errors" : []
                    },
                    status.HTTP_200_OK
                )
            
        else :
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.get(email=request.data['email'])
                
                refresh = RefreshToken.for_user(user)                    
                data = UserRegistrationSerializer(instance=user).data
                data['access_token'] = str(refresh.access_token)
                data['status'] = "VERIFIED"
                data['gender'] = "UNKNOWN"
                data['expires_at'] = refresh['exp']
                data['type'] = "CUSTOMERID"

                return Response(
                    {
                            "data": { "user" : data },
                            "status" : "ok",
                            "code" : 200,
                            "message" : "Login successfull",
                            "errors" : []
                    },
                    status.HTTP_200_OK
                )
            # return Response(serializer.validated_data, status=status.HTTP_200_OK)
            res = {
                'message' : str(serializer.errors['non_field_errors'][0]),
                'status' : "Bad Request",
                'code' : status.HTTP_400_BAD_REQUEST,
                'errors' : serializer.errors
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


