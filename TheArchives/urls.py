from django.urls import path

from . import views

urlpatterns = [
    # ex: /archives/
    path("", views.index, name="index"),
    # ex: /archives/5/
    path("<int:character_id>/", views.details, name="details")
]