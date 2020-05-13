from rest_framework import serializers
from .models import User_Input


class User_InputSerializer(serializers.ModelSerializer):
    # lft = serializers.SlugRelatedField(slug_field='lft', read_only=True)
    class Meta:
        model = User_Input
        fields = "__all__"