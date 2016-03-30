from django.views.generic import DetailView

from post.models import Post


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post.html'
