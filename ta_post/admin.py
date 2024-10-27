from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "day1",
        "day2", 
        "day3",
        "author",
        "about", 
    )

admin.site.register(Post, PostAdmin)