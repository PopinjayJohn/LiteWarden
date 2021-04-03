from django.urls import path

from . import views

app_name = "lw_reporter"
urlpatterns = [
    path("", views.index, name="index"),
]
