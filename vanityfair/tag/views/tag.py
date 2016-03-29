from django.views.generic import DetailView

from tag.models import Tag


class TagDetailView(DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'tag/detail.html'
    slug_field = "name"
