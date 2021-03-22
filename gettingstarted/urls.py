from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import admini.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    # path("", hello.views.index, name="index"),
    path("", include("admini.urls"), name="index"),
    # path("administracion", administracion.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("page/", include("admini.urls")),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/callback/', include("admini.urls")),
]
