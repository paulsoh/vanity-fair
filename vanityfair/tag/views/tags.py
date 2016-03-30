from django.views.generic import ListView

from tag.models import Tag


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tag/list.html'
