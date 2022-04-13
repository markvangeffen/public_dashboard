from django.views.generic import TemplateView
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from .forms import PostForm # add this
from .models import Post, Report


def Comment_Feed(request):
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

def Delete_Post(request, post_id):
  # check if post belongs to user
  post = Post.objects.get(id=post_id)
  if post.user == request.user:
      post.delete()
  # remove it from the database
  # redirect back to same page
  return redirect('comments_feed')

# class GerapporteerdeCommentsView(TemplateView): 
#     template_name = 'comments_feed/gerapporteerde_comments.html'

@permission_required('comments_feed.view_report', raise_exception=True)
def Gerapporteerde_Comments(request):
  return render(request, 'comments_feed/gerapporteerde_comments.html')

def Report_Post(request, post_id):
  post = Post.objects.get(id=post_id)

  report, created = Report.objects.get_or_create(reported_by=request.user, post=post)

  if created:
      report.save()

  return redirect('comments_feed')
  
@permission_required('comments_feed.view_report', raise_exception=True)
def reports(request):
  reports = Report.objects.annotate(times_reported=Count('report')).filter(times_reported__gt=0).all()

  context = {'reports' : reports}

  return render(request, 'comments_feed/gerapporteerde_comments.html', context)