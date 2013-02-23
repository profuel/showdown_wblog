from django.contrib import admin
from blog.models import Blog, Post
from apps.blog.admin_forms import PostAdminForm


# class PostInlineAdmin(admin.StackedInline):
class PostInlineAdmin(admin.TabularInline):
    model = Post
    extra = 1
    form = PostAdminForm


class BlogAdmin(admin.ModelAdmin):
    inlines = [PostInlineAdmin]


admin.site.register(Blog, BlogAdmin)
