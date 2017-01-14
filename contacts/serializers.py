from rest_framework import serializers
from contacts.models import Contact

Class SnippetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250, required=True)
    telephone_number = serializers.CharField(max_length=16, required=True)
    email = serializers.EmailField(max_length=100, required=True)
