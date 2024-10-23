from django.contrib import admin
from core.models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at',)
  list_display = ('title', 'created_at')
  search_fields = ('title', 'tags__name')
  list_filter = ('tags',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
