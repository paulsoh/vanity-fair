from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from vanityfair.views import HomeTemplateView
from user.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeTemplateView.as_view(), name="home"),

    url(r'^posts/', LoginTemplateView.as_view(), name="posts"),
    url(r'^post/', LoginTemplateView.as_view(), name="post"),

    url(r'^profile/', ProfileTemplateView.as_view(), name="profile"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^login/', LoginTemplateView.as_view(), name="login"),
    url(r'^signup/', SignupTemplateView.as_view(), name="signup"),
] + static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)
