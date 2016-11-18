from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from BBS import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,logout,authenticate
from BBS.forms import ArticleForm,handle_uploaded_file
from bbs import comment_hander
# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request,"index.html",{'articles':articles})

def category(request,category_id):
    articles = models.Article.objects.filter(category_id=category_id)
    return render(request,"index.html",{'articles':articles})


def article_detail(request,article_id):
    try:
        article_obj = models.Article.objects.get(id=article_id)
        comment_obj = models.Comment.objects.all()
    except ObjectDoesNotExist as e:
        return render(request,'404.html')
    print(article_obj)
    return render(request,'article.html',{'article_obj':article_obj,'comment_obj':comment_obj})


def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def acc_login(request):
    err_msg = ""
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # return HttpResponseRedirect('/')
            return HttpResponseRedirect(request.GET.get('next') or '/')
        else:
            err_msg = "用户名或密码错误"
    return render(request,'login.html',{'err_msg':err_msg})

def create_article(request):
    if (request.method == "POST"):
        form = ArticleForm(request.POST,request.FILES)
        if (form.is_valid()):
            data = form.clean()
            data['author_id'] = request.user.userprofile.id
            article_obj = models.Article(**data)
            article_obj.save()
            return render(request,'create_article.html',{'article_obj':article_obj})
        else:
            print('error %s' % form.errors)
    category_list = models.Category.objects.all()
    return render(request,'create_article.html',{'category_list':category_list})


def comment_post(request):
    if request.method == 'POST':
        new_comment_obj = models.Comment(
            article_id=request.POST.get('article_id'),
            parent_comment_id=request.POST.get('parent_comment_id') or None,
            comment_type=request.POST.get("comment_type"),
            user_id=request.user.userprofile.id,
            comment=request.POST.get('comment')
        )
        new_comment_obj.save()

        return HttpResponse('')

def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = comment_hander.build_tree(article_obj.comment_set.select_related())
    tree_html = comment_hander.render_comment_tree(comment_tree)
    return HttpResponse(tree_html)