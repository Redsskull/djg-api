from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'post', 'content', 'created_at', 'updated_at', 'profile_id', 'profile_image']


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')