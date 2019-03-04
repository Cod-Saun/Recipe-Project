from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms

# Create your views here.

def index(request):
    i_list=models.Playlist.objects.values_list()
    i_form = forms.PlaylistForm()

    if request.method == "POST":
        i_form = forms.PlaylistForm(request.POST)
        if i_form.is_valid():
            new_playlist = models.Playlist()
            new_playlist.Song_Name = i_form.cleaned_data["Song_Name"]
            new_playlist.Artist_Name = i_form.cleaned_data["Artist_Name"]
            new_playlist.Album_Name = i_form.cleaned_data["Album_Name"]
            new_playlist.Song_Duration = i_form.cleaned_data["Song_Duration"]
            new_playlist.save()
            i_form = forms.PlaylistForm()
    else:
        i_form = forms.PlaylistForm()

    context = {
        "body":"CINS 465 Hello World! Template",
        "item_list":i_list,
        "form":i_form
    }
    return render(request,"index.html", context=context)
