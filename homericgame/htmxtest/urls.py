from django.urls import path

from . import views

app_name="htmxtest"
urlpatterns = [
    path("", views.test, name="test"),
    path("weapon", views.weapon, name="weapon"),
]