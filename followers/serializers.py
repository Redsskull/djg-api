from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError


class FollowerSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    followed = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'created_at', 'followed_name']
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already following this user.'
            })
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['owner'] = instance.owner.username
    #     data['followed'] = instance.followed.username
    #     return data