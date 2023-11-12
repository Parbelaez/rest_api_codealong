from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from rest_api_codealong.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # Who follows who
        'owner__followed__owner__profile',
        # Who likes what
        'likes__owner__profile',
        # Who posts what
        'owner__profile',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
    ]

    search_fields = [
        'title',
        'owner__username',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]