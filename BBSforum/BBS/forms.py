from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    head_img = forms.ImageField()
    summary = forms.CharField(max_length=255,min_length=10)
    content = forms.CharField(min_length=10)
    category_id = forms.IntegerField()


def handle_uploaded_file(f):
    with open('some/file/name.txt','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)