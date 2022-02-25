from django.urls import path
from .views import ( 
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView

)

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/new/', PostCreateView.as_view(), name="post_new"),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]