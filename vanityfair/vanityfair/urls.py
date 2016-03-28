from django.conf.urls import url
from django.contrib import admin

from vanityfair.views import HomeTemplateView
from user.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeTemplateView.as_view(), name="home"),

    url(r'^login/', LoginTemplateView.as_view(), name="login"),
    url(r'^signup/', SignupTemplateView.as_view(), name="signup"),
]
