from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

class LoginTemplateView(TemplateView):

    template_name = "login.html"

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
        return redirect(reverse("home"))
