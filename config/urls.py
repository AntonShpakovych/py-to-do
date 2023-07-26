from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="tasks/", permanent=True)),
    path("tasks/", include("task.urls", namespace="task")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
