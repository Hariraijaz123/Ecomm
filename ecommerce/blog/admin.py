from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp', 'content']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['timestamp', 'updated', 'title']
    search_fields = ['title', 'content']
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)