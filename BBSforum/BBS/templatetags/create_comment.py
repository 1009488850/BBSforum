from  django import template
from django.utils.html import format_html
from BBS import models
register = template.Library()


def tree_search(d_dic,comment_obj):
    for k,v_dic in d_dic.items():
        if k == comment_obj.parent_comment: #find parent
            d_dic[k][comment_obj] = {}
            return
        else: #going deeper....;
            tree_search(d_dic[k],comment_obj)


def generate_comment_html(sub_comment_dic,margin_left_val):
    html = ""
    for k,v_dic in sub_comment_dic.items():
        userprofile = models.Comment.objects.all().select_related()
        for i in userprofile:
            if i.id == k.id:
                html += "<div style='margin-left:%spx;' class='comment-node'>" % \
                        margin_left_val + "<a href=''>" + i.user.name +"</a>"  +\
                        "   " + k.comment + "</div>"
        if v_dic:
            html += generate_comment_html(v_dic,margin_left_val+25)
    return html



@register.simple_tag
def build_comment_tree(comment_list):
    comment_dic = {}
    for comment_obj in comment_list:
        if comment_obj.parent_comment is None:#no parent
            comment_dic[comment_obj] ={}
        else: #has farther ,
            tree_search(comment_dic,comment_obj)


    html = "<div class='comment-box;'>"
    margin_left = 0
    for k,v in comment_dic.items():
        userprofile = models.Comment.objects.all()
        for i in userprofile:
            if i.id == k.id:
                html += "<div class='comment-node'>" + "<a href=''>" + i.user.name + \
                        "</a>" + "   " +  k.comment + "</div>"
                html += generate_comment_html(v,margin_left + 25)
    html += "</div>"
    return format_html(html)