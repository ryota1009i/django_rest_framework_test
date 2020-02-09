# coding: utf-8

from rest_framework import serializers

from .models import User, Entry, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    # author,commentのserializerを上書き
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('id', 'title', 'body', 'created_at', 'status', 'author')

class CommentSerializer(serializers.ModelSerializer):
    entry = EntrySerializer()
    class Meta:
        model = Comment
        fields = ('id', 'name', 'body', 'created_at', 'entry')
