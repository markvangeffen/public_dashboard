from django.contrib import admin

# Register your models here.
from .models import Post, Report

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','date_posted')
    readonly_fields=('date_posted',)
    pass

# admin.site.register(Post)
admin.site.register(Report)