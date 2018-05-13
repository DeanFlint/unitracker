from django.shortcuts import render, redirect, reverse, get_object_or_404, redirect
from .models import Bug
from .forms import CreateBugForm

# Create your views here.
def view_bugs(request):
    """ A view that renders the bugs content page """
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})
    
def view_bug(request, pk):
    """
    Create a view that returns a single bug object based on 
    the bug ID (pk) and render it to the 'view_bug.html'
    template. Or return a 404 error if the post is not found. 
    """
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, "view_bug.html", {'bug': bug})
    
def create_bug(request):
    """
    Create a view that allows us to create or edit a post depending
    if the Post ID is null or not.
    """
    if request.method == "POST":
        form = CreateBugForm(request.POST)
        if form.is_valid():
            bug = form.save()
            return redirect(view_bug, bug.pk)
    else:
        form = CreateBugForm()
    return render(request, 'post_bug.html', {'form': form})