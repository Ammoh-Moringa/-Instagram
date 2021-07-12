
from insta.forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView

@login_required(login_url='/')
def home(request):
    
    return render(request, 'index.html')

def signup(request):
    # if request.user.is_authenticated():
    #     return redirect('home')
    # else:
    #     if request.method == 'POST':
    #         form = SignupForm(request.POST)
    #         if form.is_valid():
    #             user = form.save(commit=False)
    #             user.is_active = False
    #             user.save()
    #             current_site = get_current_site(request)
    #             to_email = form.cleaned_data.get('email')
    #             send_activation_email(user, current_site, to_email)
    #             return HttpResponse('Confirm your email address to complete registration')
        form = SignUpForm()
        return render(request, 'registration/signup.html',{'form':form})



