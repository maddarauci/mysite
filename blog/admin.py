#blog/admin.py
import django.contrib.admin
from .models import Post
#from django.contrib.auth import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
'''
class DisplayAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
'''

class AuthorAdmin(django.contrib.admin.ModelAdmin):
    pass
django.contrib.admin.site.register(Post, PostAdmin)