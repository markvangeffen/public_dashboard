from django.views.generic import TemplateView

class CommentFeedView(TemplateView): 
    template_name = 'comments_feed/comments_feed.html'

class GerapporteerdeCommentsView(TemplateView): 
    template_name = 'comments_feed/gerapporteerde_comments.html'