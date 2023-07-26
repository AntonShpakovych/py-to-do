from django.urls import path

from task.views import home_page


urlpatterns = [
    path("", home_page, name="home-page")
]

app_name = "task"
