from django.shortcuts import render, redirect, reverse, get_object_or_404, redirect
from .models import Feature, FeatureComment, FeatureUserVotes
from .forms import CreateFeatureForm, CreateFeatureCommentForm, FilterView
from donate.models import Donate
from django.db.models import Sum

# Create your views here.
def view_features(request):
    """ A view that renders the bugs content page """
    user = request.user
    donation_total = Donate.objects.filter(user=user).aggregate(Sum('donation'))['donation__sum']
    if request.method == "POST":
        filterView = FilterView(request.POST)
        if filterView.is_valid() == True:
            filterView2 = request.POST.get('order_by')
            if filterView2 == ("name_az"):
                features = Feature.objects.all().order_by('name')
            elif filterView2 == ("name_za"):
                features = Feature.objects.all().order_by('-name')
            elif filterView2 == ("status_az"):
                features = Feature.objects.all().order_by('status')
            elif filterView2 == ("status_za"):
                features = Feature.objects.all().order_by('-status')
            else:
                features = Feature.objects.all().order_by('-id')
    else:
        filterView = FilterView()
        """ Filter by ID reverse - newest tickets on top by default """
        features = Feature.objects.all().order_by('-id')

    return render(request, "features.html", {"features": features, "filterView": filterView, 'donation_total': donation_total})
    
def view_feature(request, pk):
    """
    Create a view that returns a single bug object based on 
    the bug ID (pk) and render it to the 'view_bug.html'
    template. Or return a 404 error if the post is not found. 
    """
    feature = get_object_or_404(Feature, pk=pk)
    comments = FeatureComment.objects.filter(feature_id=pk)
    user = request.user
    donation_total = Donate.objects.filter(user=user).aggregate(Sum('donation'))['donation__sum']
    users_votes = FeatureUserVotes.objects.filter(featuree=feature).count()
    users_votes2 = FeatureUserVotes.objects.filter(featuree=feature, user=user).count()
    return render(request, "view_feature.html", {'feature': feature , "comments": comments, 'users_votes': users_votes, 'users_votes2': users_votes2, 'donation_total': donation_total}) 

    
def create_feature(request):
    """
    Create a view that allows us to create a bug
    """
    if request.method == "POST":
        form = CreateFeatureForm(request.POST)
        if form.is_valid():
            feature = form.save()
            return redirect(view_feature, feature.pk)
    else:
        form = CreateFeatureForm()
    return render(request, 'post_feature.html', {'form': form})
    
def add_feature_comment(request, pk):
    """ 
    Add a comment to the bug
    """
    featuree = Feature.objects.get(pk=pk)
    form = CreateFeatureCommentForm(request.POST)
    user = request.user
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.feature = featuree
            form.save()
        return redirect(view_feature, featuree.pk)
    else:
        form = CreateFeatureCommentForm()
    return render(request, 'add_comment.html', {'form': form})
    
def feature_vote(request, pk):
    """
    Allow user to vote for bug if not voted on this one before.
    """
    featuree = Feature.objects.get(pk=pk)
    user= request.user
    user_vote = FeatureUserVotes(featuree=featuree, user=user)
    user_vote.save()
    return redirect(view_feature, featuree.pk)


