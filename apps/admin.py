"""
admin file
"""
from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class OrderAdmin(admin.ModelAdmin):
    """
    modify to user admin for user display according
    """
    list_display = ['pmid', 'title', 'abstract', 'keywords', 'full_text_link']

