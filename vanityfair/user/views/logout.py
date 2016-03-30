from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
        return redirect(reverse('home'))
