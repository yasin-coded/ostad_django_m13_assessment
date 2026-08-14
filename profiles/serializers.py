from os import read

from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'address', 'bio']
        read_only_fields = ['user']