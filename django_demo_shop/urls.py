from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from catalog.views import page_does_not_exists, server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('', include('shop.urls', namespace='shop'))
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = page_does_not_exists
handler500 = server_error
