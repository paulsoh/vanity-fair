from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from post.models import Comment, Post
from api.serializers import CommentSerializer


class CommentAPIView(APIView):

    def get(self, request, **kwargs):
        post = Post.objects.get(
            pk=kwargs.get('pk'),
        )

        comments = post.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        data = request.data

        post = Post.objects.get(
            pk=data.get('post'),
        )

        comment = post.comment_set.create(
            user=request.user,
            content=data.get('content'),
        )

        serializer = CommentSerializer(comment)
        if CommentSerializer(data=serializer.data):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
