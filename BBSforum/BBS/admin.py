from django.contrib import admin
from BBS import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','head_img','title','author','summary','hidden','publish_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','parent_comment','user','comment','date')

admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)