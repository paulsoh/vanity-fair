from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from user.models import User


class SignupTemplateView(TemplateView):

    template_name = "signup.html"

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                password=password,
            )
        
        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)

        return redirect(reverse("home"))
