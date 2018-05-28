from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DonationForm, DonateValueForm
from .models import Donate
from django.conf import settings
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def donate(request):
    if request.method=="POST":
        donation_form = DonationForm(request.POST)
        donate_value_form = DonateValueForm(request.POST)
        
        if donate_value_form.is_valid() and donation_form.is_valid():
            donation_value = donate_value_form.save(commit=False)
            user = request.user
            donation_value.user = user
            total = donation_value.donation
            donation_value.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.username,
                    card = donation_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully donate, thank you!")
                return render(request, "index.html")
            else:
                messages.error(request, "Unable to take payment")
        
        else:
            print(donation_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        donation_form = DonationForm()
        donate_value_form = DonateValueForm
        
    return render(request, "donate.html", {'donation_form': donation_form, 'donate_value_form': donate_value_form, 'publishable': settings.STRIPE_PUBLISHABLE})