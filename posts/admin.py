from django.contrib import admin
from .models import Posts

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'post_date')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts, PostAdmin)