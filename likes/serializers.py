from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for Like objects.
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'post',
            'created_at'
        ]
    
    def create(self, validated_data):
        """
        Create and return a new Like instance, given the validated data.
        """
        try:
            return super().create(validated_data)
        except IntegrityError  as e:
            raise serializers.ValidationError({
                'detail':'You already liked this post'
            }) from e