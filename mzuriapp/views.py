from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mzuriapp.forms import UserForm, ArtistForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return redirect(artist_home)

@login_required(login_url='/artist/sign-in/')
def artist_home(request):
    return render(request, 'artist/home.html', {})

def artist_sign_up(request):
    user_form = UserForm()
    artist_form = ArtistForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        artist_form = ArtistForm(request.POST, request.FILES)

        if user_form.is_valid() and artist_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_artist = artist_form.save(commit=False)
            new_artist.user = new_user
            new_artist.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(artist_home)

    return render(request, 'artist/sign_up.html', {

        "user_form": user_form,
        "artist_form": artist_form
    })
