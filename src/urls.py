from django.urls import include, path

urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.locations.urls')),
]
