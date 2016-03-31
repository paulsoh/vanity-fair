from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from vanityfair.views import HomeTemplateView
from user.views import *
from post.views import *
from tag.views import *

from api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeTemplateView.as_view(), name="home"),

    url(r'^posts/$', PostListView.as_view(), name="posts"),
    url(r'^posts/new/$', PostCreateView.as_view(), name="new-post"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post"),
    url(r'^posts/(?P<pk>\d+)/like/$', HomeTemplateView.as_view(), name="like"),


    url(r'^tags/$', TagListView.as_view(), name="tags"),
    url(r'^tags/(?P<slug>\w+)/$', TagDetailView.as_view(), name="tags-detail"),

    url(r'^profile/', ProfileTemplateView.as_view(), name="profile"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^login/', LoginTemplateView.as_view(), name="login"),
    url(r'^signup/', SignupTemplateView.as_view(), name="signup"),

    url(r'^api/posts/(?P<pk>\d+)/comments/$', CommentAPIView.as_view(), name="comments"),
] + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    ) + static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
        )
