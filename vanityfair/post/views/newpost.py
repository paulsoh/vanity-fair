from django.views.generic import CreateView

from post.models import Post


class PostCreateView(CreateView):

    template_name = "post/newpost.html"
    model = Post

    fields = (
        'image',
        'content',
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        tags = self.request.POST.get('tags').split()
        form.instance._tags = tags
        form.instance.image = self.request.FILES['image']
        return super(PostCreateView, self).form_valid(form)
