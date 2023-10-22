from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('comment/<int:pk>/', CreateComment.as_view(), name="create_comment"),
    path('', HomeView.as_view(), name='home'),
    # path('<str:app_name>/<int:category_pk>/<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('<str:app_name>/<slug:cat_slug>/<slug:slug>', PostDetailView.as_view(), name="post_detail"),
    re_path(r'^blog/$', PostListView.as_view(), name="post_list"),
    path('favorites/', FavoritesListView.as_view(), name="favorites_list"),
    path('blog/category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('blog/category/', CategoryListView.as_view(), name="category_list"),
    path('tags/<slug:slug>', TagDetailView.as_view(), name="tag_detail"),
    path('blog/post-create/', PostCreateView.as_view(), name='post_create'),
    # path('blog/send/', PostCreateSend.as_view(), name='send'),
    # path('<str:app_name>/<slug:cat_slug>/<slug:slug>', views.PostEditView, name='post_edit'),
    path('search/', SearchResultsListView.as_view(), name='search_result'),

]
