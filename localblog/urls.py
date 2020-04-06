from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url

from posts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    url(r'^add/', views.index, name='index'),
    path('edit/<slug:slug>/', views.editPost, name='edit_post'),
    path('', include('posts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
