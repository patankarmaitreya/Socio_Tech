from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("assist/", views.assist, name="assist"),
    path("adopt", views.adopt, name="adopt"),
    path("medic", views.medic, name="medic"),
    path("help", views.help, name="help"),
]