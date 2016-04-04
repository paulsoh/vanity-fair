from django.views.generic import ListView

from post.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/posts.html'

    def get_queryset(self):
        return Post.objects.order_by('-social_score')
