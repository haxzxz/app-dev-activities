from django.contrib import admin
from .models import Post, Comment
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

def mark_as_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)
mark_as_featured.short_description = "Mark selected posts as Featured"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'created_at', 'is_featured')
    list_filter = ('is_featured', 'created_at', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    inlines = [CommentInline]

    actions = [mark_as_featured]
    
    readonly_fields = ('created_at', 'updated_at') 

    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "content", "author")
        }),
        ("Settings", {
            "fields": ("is_featured",)
        }),
        ("Dates", {
            "fields": ("created_at",)
        }),
    )
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commenter', 'created_at')
    search_fields = ('commenter', 'text')
    list_filter = ('created_at',)

# Register your models here.
