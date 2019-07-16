from django.contrib import admin

from django.urls import include, path

urlpatterns = [
    path('', include('static_website.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
]
