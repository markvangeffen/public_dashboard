from django.views.generic import TemplateView
from django.shortcuts import render, redirect 
from .forms import PostForm # add this
from .models import Post

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
    posts = Post.objects.filter(hidden=False).order_by('-date_posted').all()

    context = {'form' : form, 'posts' : posts}

  return render(request, 'comments_feed/comments_feed.html', context)

def delete_post(request, post_id):
  # check if post belongs to user
  post = Post.objects.get(id=post_id)
  if post.user == request.user:
      post.delete()
  # remove it from the database
  # redirect back to same page
  return redirect('comments_feed')
  