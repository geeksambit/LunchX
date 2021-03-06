
import jwt
from rest_framework import serializers
from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate



User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    It's user registration model serializer.
    """
    confirm_password = serializers.CharField(style={'input_type': 'password'},
        max_length=20, min_length=8, required=True, write_only = True,)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 
            'id', 'is_active', 'role', 'date_joined', 'confirm_password',
            'auth_provider')
        read_only_fields = ('id', 'is_active', 'date_joined',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, data):
        user = User.objects.filter(email=data['email']).exists()
        if user:
            raise serializers.ValidationError(
                "Account with email {} already exists. Please login to continue".format(data['email'])
            )
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data


    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.is_active = True
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'},
        max_length=20, min_length=2, required=True, write_only = True,)

    def validate(self, data):
        user = User.objects.filter(email=data['email']).exists()
        if not user:
            raise serializers.ValidationError(
                "Email doesn't exists. Please sign up to continue."
            )
        
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError(
                "Invalid credentials. Please try again!"
            )
        return data


##seriallizer for social login

# from django.conf import settings
# from rest_framework import serializers
# from utils import google, facebook
# from utils.register import register_social_user
# import os
# from rest_framework.exceptions import AuthenticationFailed



class GoogleSocialAuthSerializer(serializers.Serializer):
    pass
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:

            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        # first_name =user_data['name']
        provider = 'google'


        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)




