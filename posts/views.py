from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
      comments_count=Count('comment', distinct=True),
      like_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter,
                       DjangoFilterBackend]
    filterset_fields = ['owner__followed__owner__profile', 'likes__owner__profile', 'owner__profile']
    search_fields = ['title', 'owner__username']
    ordering_fields = ['comment_count', 'like_count', 'created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()