
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("app1/",include("hello.urls")),
    path("home/",include("home.urls")),
    path("about/",include("about.urls")),
    path("contact/",include("contact.urls")),
    path("demo/",include("demo.urls")),
    path("auth/",include("accounts.urls"))
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
