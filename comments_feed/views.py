from django.views.generic import TemplateView
from django.shortcuts import render, redirect 
from .forms import PostForm # add this

# class CommentFeedView(TemplateView): 
#     template_name = 'comments_feed/comments_feed.html'

class GerapporteerdeCommentsView(TemplateView): 
    template_name = 'comments_feed/gerapporteerde_comments.html'

def CommentFeedView(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user 
      post.save()
      return redirect('comments_feed')
  else:
    form = PostForm()

  context = {'form' : form}

  return render(request, 'comments_feed/comments_feed.html', context)


