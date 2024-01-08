from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("posts", views.AllPostView.as_view(), name="postpage"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="detailpage"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
