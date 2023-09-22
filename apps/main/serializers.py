from rest_framework import serializers
from .models import Post, Like, Comment


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['username', 'text', 'created_at']

    created_at = serializers.DateTimeField(format="%H:%M, %m/%d/%Y", read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'username', 'like', 'text', 'created_at']

    created_at = serializers.DateTimeField(format="%H:%M, %m/%d/%Y", read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    id = serializers.IntegerField(read_only=True)
    like = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_like(obj):
        return obj.likes.count()


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'like', 'text', 'created_at', 'comments']

    created_at = serializers.DateTimeField(format="%H:%M, %m/%d/%Y", read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    id = serializers.IntegerField(read_only=True)
    like = serializers.SerializerMethodField(read_only=True)
    comments = CommentSerializer(many=True)

    @staticmethod
    def get_like(obj):
        return obj.likes.count()
