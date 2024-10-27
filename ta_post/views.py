from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy

class TutorListView(ListView):
    model = Post
    template_name = "home.html"

class TutorDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class TutorCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "day1", "day2", "day3", "classes", "about", ]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

class TutorUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "day1", "day2", "day3", "about", "classes", ]
