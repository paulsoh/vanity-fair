from django.views.generic import View
from django.shortcuts import redirect

from post.models import Like, Post


class ReactionView(View):

    def get(self, request, **kwargs):
        post_id = kwargs.get('pk')
        reaction_type = kwargs.get('reaction')
        if reaction_type == 'like':
            reaction = 'LI'
        elif reaction_type == 'dislike':
            reaction = 'DL'
        else:
            reaction = 'WA'
        post = Post.objects.get(pk=post_id)
        user = request.user
        Like.objects.create(
            post=post,
            user=user,
            reaction=reaction,
        )

        return redirect(post)
