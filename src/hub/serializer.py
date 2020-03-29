from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'owner'
        )


"""from django import forms


class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'description'
        )"""
