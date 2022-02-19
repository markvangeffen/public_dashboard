from django.urls import path
from .views import CommentFeedView, GerapporteerdeCommentsView

urlpatterns = [
    path('comments_feed/', CommentFeedView.as_view(), name='comments_feed'),
    path('gerapporteerde_comments/', GerapporteerdeCommentsView.as_view(), name='gerapporteerde_comments'),    
]