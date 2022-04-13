from django.urls import path
from .views import Comment_Feed, Gerapporteerde_Comments, Delete_Post, Report_Post

urlpatterns = [
    path('comments_feed/', Comment_Feed, name='comments_feed'),
    path('delete/<post_id>/', Delete_Post, name='delete_post'),
    # path('gerapporteerde_comments/', GerapporteerdeCommentsView.as_view(), name='gerapporteerde_comments'),
    path('gerapporteerde_comments/', Gerapporteerde_Comments, name='gerapporteerde_comments'),
    path('report_post/<post_id>/', Report_Post, name='report_post'),
]