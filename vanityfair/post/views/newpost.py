from django.views.generic import CreateView

from post.models import Post


class PostCreateView(CreateView):

    template_name = "post/newpost.html"
    model = Post

    fields = (
        'content',
    )
