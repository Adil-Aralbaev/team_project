from rest_framework import serializers

from .models import Post, Comment, Rating

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['user', ]
        fields = '__all__'