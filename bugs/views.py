from django.shortcuts import render, redirect, reverse, get_object_or_404, redirect
from .models import Bug, Comment, UserVotes
from .forms import CreateBugForm, CreateCommentForm, FilterView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Create your views here.
def view_bugs(request):
    """ A view that renders the bugs content page """
    if request.method == "POST":
        filterView = FilterView(request.POST)
        if filterView.is_valid() == True:
            filterView2 = request.POST.get('order_by')
            if filterView2 == ("name_az"):
                bugs = Bug.objects.all().order_by('name')
            elif filterView2 == ("name_za"):
                bugs = Bug.objects.all().order_by('-name')
            elif filterView2 == ("status_az"):
                bugs = Bug.objects.all().order_by('status')
            elif filterView2 == ("status_za"):
                bugs = Bug.objects.all().order_by('-status')
            else:
                bugs = Bug.objects.all().order_by('-id')
    else:
        filterView = FilterView()
        """ Filter by ID reverse - newest tickets on top by default """
        bugs = Bug.objects.all().order_by('-id')

    return render(request, "bugs.html", {"bugs": bugs, "filterView": filterView})
    
def view_bug(request, pk):
    """
    Create a view that returns a single bug object based on 
    the bug ID (pk) and render it to the 'view_bug.html'
    template. Or return a 404 error if the post is not found. 
    """
    bug = get_object_or_404(Bug, pk=pk)
    comments = Comment.objects.filter(bug_id=pk)
    user = request.user
    users_votes = UserVotes.objects.filter(bugg=bug).count()
    users_votes2 = UserVotes.objects.filter(bugg=bug, user=user).count()
    return render(request, "view_bug.html", {'bug': bug , "comments": comments, 'users_votes': users_votes, 'users_votes2': users_votes2}) 

    
def create_bug(request):
    """
    Create a view that allows us to create a bug
    """
    if request.method == "POST":
        form = CreateBugForm(request.POST)
        if form.is_valid():
            bug = form.save()
            return redirect(view_bug, bug.pk)
    else:
        form = CreateBugForm()
    return render(request, 'post_bug.html', {'form': form})
    
def add_comment(request, pk):
    """ 
    Add a comment to the bug
    """
    bugg = Bug.objects.get(pk=pk)
    form = CreateCommentForm(request.POST)
    user = request.user
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.bug = bugg
            form.save()
        return redirect(view_bug, bugg.pk)
    else:
        form = CreateCommentForm()
    return render(request, 'add_comment.html', {'form': form})
    
def user_vote(request, pk):
    """
    Allow user to vote for bug if not voted on this one before.
    """
    bugg = Bug.objects.get(pk=pk)
    user= request.user
    user_vote = UserVotes(bugg=bugg, user=user)
    user_vote.save()
    return redirect(view_bug, bugg.pk)


