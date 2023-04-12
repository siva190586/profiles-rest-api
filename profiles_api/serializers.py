from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes the profile fields to manage"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwagrs = {
            'password': {
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }
    
    def create(self, validated_data):
        """create and return user data"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle user data update"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)