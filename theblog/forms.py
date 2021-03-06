from django import forms
from .models import Post,Category

choices=Category.objects.all().values_list('name','name')
choices_list=[]
for i in choices:
    choices_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','auther','category','body','snippet','header_image')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'auther': forms.Select(attrs={'class':'form-control'}),
            'auther': forms.TextInput(attrs={'class': 'form-control','type':'hidden','id':'current'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.TextInput(attrs={'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','category','body','snippet','header_image')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }