from rest_framework import views, response, status, permissions, generics
from .models import Post, Like, Comment
from .serializers import PostSerializer, PostDetailSerializer


class PostAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        data['user'] = user.id
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class PostsAPI(generics.ListAPIView):
    queryset = Post.objects.order_by('-likes')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostRetrieveAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        post = Post.objects.filter(id=self.kwargs.get('pk')).first()
        like = Like.objects.filter(user=user, post=post).first()
        serializer = PostSerializer(post)
        if like:
            like.delete()
        else:
            Like.objects.create(user=user, post=post)
        return response.Response(serializer.data)

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(id=self.kwargs.get('pk')).first()
        serializer = PostDetailSerializer(post)
        data = serializer.data
        like = Like.objects.filter(user=self.request.user, post=post).first()
        if like:
            data['liked'] = True
        else:
            data['liked'] = False
        return response.Response(data)


class CommentAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = Post.objects.filter(id=self.kwargs.get('pk')).first()
        Comment.objects.create(user=self.request.user, post=post, text=self.request.data['text'])
        return response.Response({'success': True})
