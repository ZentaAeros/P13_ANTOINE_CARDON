from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('lettings.urls', namespace="lettings")),
    path('', include('profiles.urls', namespace="profiles")),
    path('', include('home.urls', namespace="home")),
    path('admin/', admin.site.urls),
]
