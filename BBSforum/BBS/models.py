from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    '''
    帖子表
    '''
    title = models.CharField(u'文章标题',max_length=255,unique=True)
    category = models.ForeignKey("Category",verbose_name=u"版块")
    head_img = models.ImageField(u'图片',upload_to="img")
    summary = models.CharField(u'总结',max_length=255)
    content = models.TextField(u'文章内容')
    author = models.ForeignKey("UserProfile")
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=True)
    priority = models.IntegerField(u'优先级',default=1000)

    def __str__(self):
        return "<%s ,%s>" %(self.title,self.author)

class Comment(models.Model):
    '''
    评论表
    '''
    article = models.ForeignKey(Article)
    user = models.ForeignKey("UserProfile")
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField(u'评论内容',max_length=1000)
    parent_comment = models.ForeignKey('Comment',related_name="p_comment",blank=True,null=True)
    # parent_comment = models.ForeignKey('self',related_name="p_comment")
    def __str__(self):
        return "(<%s,%s,%s>)" %(self.comment,self.user,self.date)

class ThumbUp(models.Model):
    '''
    点赞
    '''
    article = models.ForeignKey('Article')
    user =  models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<%s>" %self.user

class Category(models.Model):
    '''
    帖子版块
    '''
    name = models.CharField(u'帖子版块名',max_length=64,unique=True)
    admin = models.ForeignKey("UserProfile")
    def __str__(self):
        return self.name



class UserProfile(models.Model):
    '''
    账户信息表
    '''
    user = models.OneToOneField(User)
    name = models.CharField(u'用户名',max_length=32)
    groups = models.ManyToManyField("UserGroup")
    friends = models.ManyToManyField('self',related_name='my_friends')
    def __str__(self):
        return "(<%s,%s>)" %(self.user,self.name)



class UserGroup(models.Model):
    '''
    用户组
    '''
    name = models.CharField(u'用户组名',max_length=64,unique=True)
    def __str__(self):
        return self.name