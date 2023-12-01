from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # tells Django to serve static files from the STATIC_ROOT folder on dev server