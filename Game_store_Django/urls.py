from django.contrib import admin
from django.urls import path, include
from games.views import IndexView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', include('games.urls', namespace='games')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))