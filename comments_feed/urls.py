from django.urls import path
from .views import CommentFeedView, GerapporteerdeCommentsView, delete_post

urlpatterns = [
    path('comments_feed/', CommentFeedView, name='comments_feed'),
    path('delete/<post_id>/', delete_post, name='delete_post'),
    path('gerapporteerde_comments/', GerapporteerdeCommentsView.as_view(), name='gerapporteerde_comments'),
]