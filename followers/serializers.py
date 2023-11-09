from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for Follower objects.
    The create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'followed',
            'created_at', 'followed_name'
        ]
    
    def create(self, validated_data):
        """
        Create and return a new Follower instance, given the validated data.
        """
        try:
            return super().create(validated_data)
        except IntegrityError  as e:
            raise serializers.ValidationError({
                'detail':'You already followed this user'
            }) from e