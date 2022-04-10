from django.contrib import admin

# Register your models here.
from .models import Post, Report
from authO.admin import User, UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','date_posted')
    readonly_fields=('date_posted',)
    pass

# admin.site.register(Post)
admin.site.register(Report)