from django.urls import path
from .views import Comment_Feed, Gerapporteerde_Comments, Delete_Post, Report_Post, Hide_Post, Block_User

urlpatterns = [
    path('comments_feed/', Comment_Feed, name='comments_feed'),
    path('delete/<post_id>/', Delete_Post, name='delete_post'),
    # path('gerapporteerde_comments/', GerapporteerdeCommentsView.as_view(), name='gerapporteerde_comments'),
    path('gerapporteerde_comments/', Gerapporteerde_Comments, name='gerapporteerde_comments'),
    path('report_post/<post_id>/', Report_Post, name='report_post'),
    path('hide_post/<post_id>/', Hide_Post, name='hide_post'),
    path('block_user/<user_id>/', Block_User, name='block_user'),
]