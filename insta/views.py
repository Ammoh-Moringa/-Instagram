from insta.forms import SignUpForm
from insta.models import Image, Post
from django.shortcuts import render,redirect

# Create your views here.
from django.http  import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .emails import send_activation_email
from .tokens import account_activation_token

def home(request):
    images = Image.get_all_images()
    
    return render(request, 'index.html', {'images':images})
def signup(request):
    form = SignUpForm()
    return render(request, 'registration/signup.html',{'form':form})
  

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Post.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
