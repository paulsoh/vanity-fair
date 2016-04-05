from django.views.generic import TemplateView

from post.models import Post


class HomeTemplateView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.order_by('-social_score')[0]
        return context
