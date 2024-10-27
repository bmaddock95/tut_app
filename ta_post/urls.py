from django.urls import path
from .views import TutorListView, TutorDetailView, TutorCreateView, TutorUpdateView

urlpatterns = [
    path("post/new/", TutorCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", TutorDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", TutorUpdateView.as_view(), name="post_edit"),
    path("", TutorListView.as_view(), name="home"),
]