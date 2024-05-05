from django import forms
from .models import Comment, Post, Image
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from django_ckeditor_5.fields import CKEditor5Field


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('name', 'email', 'message', 'captcha')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя *', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email *', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Текст', 'class': 'form-control'}),
        }


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'keywords',
                  'category', 'tags', 'main_image', 'intro', 'text', 'is_favorite', 'status']
        # fields = '__all__'
        # exclude = ['pub_at', 'changed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок *', 'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'placeholder': 'URL *', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': 'Описание *', 'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'placeholder': 'Ключевые слова *', 'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'placeholder': 'Интро *', 'class': 'form-control'}),
            'text ': CKEditor5Field(max_length=8000),
            'main_image': forms.ClearableFileInput(attrs={'class': 'form-control',}),

        }
    images = forms.FileField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'multiple': '', 'accept': "image/jpeg, image/png, image/gif"})
                              )