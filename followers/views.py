from rest_framework import generics, permissions
from rest_api_codealong.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetails(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = Follower.objects.all()