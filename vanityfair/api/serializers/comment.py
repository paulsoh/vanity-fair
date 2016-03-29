from rest_framework import serializers

from post.models import Comment
from user.models import User


class CommentSerializer(serializers.ModelSerializer):

    # username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = (
            'content',
            'post',
            'user',
        )

    def save(self):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return super(CommentSerializer, self).save()
