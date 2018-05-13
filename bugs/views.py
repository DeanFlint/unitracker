from django.shortcuts import render, redirect, reverse
from .models import Bug

# Create your views here.
def view_bugs(request):
    """ A view that renders the bugs content page """
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})