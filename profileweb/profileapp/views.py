from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from .models import UserProfile  # Import UserProfile model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserProfile

# Create your views here.


def index(request):
    return render(request,"index.html")
def forgot(request):
    return render(request,"forgotpassword.html")
def otprequest(request):
    return render(request,"otprequest.html")
def create_account(request):
    return render(request,"create_account.html")



# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('view_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})


# profiles/views.py

from django.shortcuts import render, redirect
from django.views import View
from .forms import UserProfileForm, UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserRegistrationForm
from django.contrib.auth import login


from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse  # Import HttpResponse

from .forms import UserProfileForm, UserRegistrationForm

def registration_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('homepage')
        else:
            # Print the form errors to the console
            print(f"User form errors: {user_form.errors}")
            print(f"Profile form errors: {profile_form.errors}")

            # Return a response indicating something went wrong
            return HttpResponse("Something went wrong during registration. Please check the console for details.")

    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'create_account.html', {'user_form': user_form, 'profile_form': profile_form})





@login_required
def view_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'view_profile.html', {'user_profile': user_profile})
    except UserProfile.DoesNotExist:
        # Handle the case where the profile does not exist
        return render(request, 'index.html')



@login_required
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile does not exist
        return redirect('create_profile')  # Redirect to a view for creating a profile

    # Check if the user making the request is the owner of the profile
    if request.user != user_profile.user:
        # Handle the case where the user is not authorized to edit this profile
        return render(request, 'profiles/unauthorized.html')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        # Populate the form with the existing profile information
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

# def registration_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page or home page
#             return redirect('homepage')  # Replace 'home' with your actual home URL
#         else:
#             print(form.errors)
#
#     else:
#         form = UserRegistrationForm()
#
#     return render(request, 'create_account.html', {'form': form})
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET",'POST'])
def api_account(request):
    if request.data:
        recieved=request.data
        return Response({"message":"hi",'data':recieved})
    else:
        return Response({"data":"NO data"})



