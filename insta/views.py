from insta.forms import CommentForm, ImageForm, ProfileForm, SignupForm
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
from .models import Image, Profile, Comment

def home(request):
    images = Image.get_all_images()
    
    return render(request, 'index.html', {'images':images})
def signup(request):
     if request.method == 'POST':
         form = SignupForm(request.POST)
         if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            to_email = form.cleaned_data.get('email')
            send_activation_email(user, current_site, to_email)
         return redirect('login')
     else:
         form = SignupForm()
     return render(request, 'registration/signup.html',{'form':form})
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # form = LoginForm()
#         # return redirect('home')
#         return HttpResponse('registration/login.html')
#     else:
#         return HttpResponse('Activation link is invalid')
    
def profile(request, username):
    profile = User.objects.get(username=username)
    # print(profile.id)
    # try:
    #     profile_details = Profile.get_by_id(profile.id)
    # except:
    #     profile_details = Profile.filter_by_id(profile.id)
    # images = Image.get_profile_images(profile.id)
    # title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', { 'profile':profile})

@login_required(login_url='/accounts/login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            # print(f'image is {upload.image}')
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = ImageForm()
    
    return render(request, 'profile/upload_image.html', {'form':form})

@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile.html')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})


def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})

def new_image(request):
    current_user =request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = current_user
            image.save()
            return redirect("home")
    else:
        form = ImageForm()
    return render (request, 'new_image.html', {"form":form})




