import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from .forms import CommentForm, PostCreateForm
#  PostCreateFullForm
from contact.forms import ContactUsForm
from .models import Post, Category, Comment, Tag, Image
from contact.models import HomeHeroSlogans


class HomeView(TemplateView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['free_latest_posts'] = Post.objects.select_related('category', 'author').filter(
            status='published').order_by(
            '-pub_at')[:3]
        context['categories'] = Category.objects.all()
        context['hero_one'] = HomeHeroSlogans.objects.all()
        context['contact_us_form'] = ContactUsForm
        context['title'] = 'Правильный ремонт квартир'
        context['nbar'] = 'home'
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    # list_categories = Category.objects.all()
    queryset = Category.objects.all()
    context_object_name = 'my_category_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['num_cat'] = Category.objects.count()
        context['url'] = 'category/'
        return context


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.post.all
        context['main_title'] = self.object.name
        return context


class PostListView(ListView):
    """
    обобщённое(generic) отображение ищет файл шаблона /application_name/the_model_name_list.html
    (catalog/book_list.html, в данном случае) внутри
    директории приложения /application_name/templates/ (у нас - /catalog/templates/)
    """
    model = Post
    paginate_by = 9
    context_object_name = 'post_list'  # ваше собственное имя переменной контекста в шаблоне
    # queryset = Book.objects.filter(title__icontains='а')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    queryset = Post.objects.select_related('category', 'author').filter(status='published', is_favorite=False).order_by(
        '-pub_at')

    template_name = 'blog/post_list.html'  # Определение имени вашего шаблона и его расположения

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super().get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        # context['now_data'] = datetime.datetime.now()
        context['nbar'] = 'blog'  # 'nbar' make active in style
        context['main_title'] = 'блог'  # для navbar
        return context


class FavoritesListView(PostListView):  # Наследование от PostListView
    queryset = Post.objects.select_related('category', 'author').filter(status='published', is_favorite=True).order_by(
        '-pub_at')

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super().get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        # context['raw_list'] = Post.objects.all()
        context['nbar'] = 'favorites'
        context['main_title'] = 'наши работы'
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    # slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views_count += 1
        self.object.save()
        context['form'] = CommentForm
        context['images'] = self.object.get_images
        context['youtube'] = self.object.get_youtube
        context['comments'] = self.object.get_comments
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # сам comment->post->get_absolute_url()
        return self.object.post.get_absolute_url()


class TagDetailView(DetailView):
    context_object_name = "tag"
    template_name = 'blog/tag_detail.html'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_title = self.object.name
        context['tag_name'] = main_title
        context['posts'] = self.object.post.all
        context['main_title'] = main_title  # for navbar
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            Image.objects.create(post=post, image=image)
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCreateForm
        context['main_title'] = 'Добавление статьи'
        context['nabr'] = 'new-post'
        return context


class SearchResultsListView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

    # queryset = Post.objects.select_related('category', 'author').filter(status='published', title__icontains="Фото").order_by(
    #     '-pub_at')

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(Q(title__icontains=query) & Q(status='published'))
        return ''


class PostEditView:
    pass
