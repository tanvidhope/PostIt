from django.contrib.auth.models import User
from rest_framework import serializers

from articles.models import Article

'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
'''


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'author', 'body', 'date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username', 'articles')
        fields = ('id', 'username', 'email')
