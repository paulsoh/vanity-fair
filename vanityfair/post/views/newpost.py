from django.views.generic import CreateView

from post.models import Post


class PostCreateView(CreateView):

    template_name = "post/newpost.html"
    model = Post

    fields = (
        'video_url',
        'thumbnail',
        'content',
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.FILES.get('thumnail', None):
            form.instance.thumbnail = self.request.FILES['thumbnail']
        return super(PostCreateView, self).form_valid(form)
