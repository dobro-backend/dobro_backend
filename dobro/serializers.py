from django.contrib.auth.models import User
from rest_framework import serializers
from dobro.models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('login', 'email', 'password')
